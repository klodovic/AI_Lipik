import numpy as np
from pathlib import Path
import logging
import collections

# --- KONFIGURACIJA ---
BASE_DIR = Path("D:/copernicus-zagreb")
PATCH_DIR = BASE_DIR / "data/patches_c4"
OUT_DIR = BASE_DIR / "data/batches_train"
SEQ_LEN = 5  # 4 godine ulaz + 1 godina cilj
BATCH_SIZE = 1  # Broj sekvenci po batchu (ovisno o memoriji) 

OUT_DIR.mkdir(parents=True, exist_ok=True)

# --- LOGIRANJE SETUP ---
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
log_file = BASE_DIR / "batching.log"

file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setFormatter(log_formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def create_sequences():
    logging.info("=== ZAPOČINJEM GRUPIRANJE PATCHEVA ===")
    
    all_files = list(PATCH_DIR.glob("*.npz"))
    logging.info(f"Pronađeno ukupno {len(all_files)} patcheva na disku.")

    # Grupiranje po lokacijama (tile + koordinate)
    locations = collections.defaultdict(list)
    for f in all_files:
        parts = f.stem.split('_')
        # Ključ je npr: T33TWL_y128_x256
        loc_id = "_".join(parts[1:]) 
        locations[loc_id].append(f)
    
    logging.info(f"Identificirano {len(locations)} jedinstvenih geografskih lokacija.")

    sequences = []
    batch_count = 0
    total_seq_count = 0

    logging.info("Slažem vremenske sekvence (4+1)...")

    for loc_id, files in locations.items():
        # Sortiranje po godinama (2016, 2017, 2018...)
        sorted_files = sorted(files, key=lambda x: int(x.stem.split('_')[0]))
        
        if len(sorted_files) < SEQ_LEN:
            continue # Preskoči ako lokacija nema pokriveno barem 5 godina
            
        for i in range(len(sorted_files) - SEQ_LEN + 1):
            window = sorted_files[i : i + SEQ_LEN]
            
            try:
                seq_data = []
                for f in window:
                    # Svaki f je [4, 64, 64]
                    data = np.load(f)['x']
                    seq_data.append(data)
                
                # Stack u [5, 4, 64, 64]
                sequences.append(np.stack(seq_data))
                
            except Exception as e:
                logging.error(f"Greška pri čitanju lokacije {loc_id}: {e}")
                continue
            
            # Spremanje batcha
            if len(sequences) >= BATCH_SIZE:
                batch_count += 1
                batch_arr = np.stack(sequences) # [100, 5, 4, 64, 64]
                out_path = OUT_DIR / f"batch_{batch_count:04d}.npz"
                np.savez_compressed(out_path, data=batch_arr)
                
                total_seq_count += len(sequences)
                sequences = []
                
                if batch_count % 10 == 0:
                    logging.info(f"Spremljeno {batch_count} batcheva... (Ukupno sekvenci: {total_seq_count})")

    # Spremanje preostalih sekvenci koje nisu napunile cijeli BATCH_SIZE
    if sequences:
        batch_count += 1
        batch_arr = np.stack(sequences)
        out_path = OUT_DIR / f"batch_{batch_count:04d}.npz"
        np.savez_compressed(out_path, data=batch_arr)
        total_seq_count += len(sequences)

    logging.info(f"=== GOTOVO ===")
    logging.info(f"Ukupno kreirano sekvenci: {total_seq_count}")
    logging.info(f"Prosječno sekvenci po lokaciji: {total_seq_count/len(locations):.2f}")
    logging.info(f"Svi batchevi su u: {OUT_DIR}")

if __name__ == "__main__":
    create_sequences()