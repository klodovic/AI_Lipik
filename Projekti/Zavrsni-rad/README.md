# Urban Growth Prediction - Zagreb 2050 
**Deep Learning sustav za simulaciju i analizu urbanizacije koristeći satelitske podatke.**

Ovaj projekt koristi napredne tehnike računalnog vida i umjetne inteligencije za praćenje transformacije grada Zagreba. Cilj je dokumentirati potiskivanje prirode pod naletom urbanizacije te predvidjeti buduće trendove širenja gradskog betona.

[![Video Presentation](https://i.ytimg.com/vi/uDxlzmlc52k/maxresdefault.jpg)](https://www.youtube.com/watch?v=uDxlzmlc52k)
*Kliknite na sliku iznad za pokretanje video prezentacije na YouTube-u (preporučeno: desni klik -> otvori u novoj kartici).*


## 1. Opis problema i cilj projekta
Glavni izazov ovog projekta je precizno predviđanje i vizualizacija urbanog širenja grada Zagreba. Naglasak je na detekciji gubitka zelenih površina (vegetacije) i pretvaranju istih u izgrađena područja (betonizacija).

**Cilj:** Razviti sustav koji koristi povijesne satelitske podatke (2016-2024) kako bi generirao vizualne projekcije urbanizacije za 2027. i 2050. godinu. Projekt služi kao alat za pomoć pri urbanističkom planiranju i zaštiti okoliša.

## 2. Podaci (Dataset)
* **Tip podataka:** Multispektralne snimke (L2A - Bottom-Of-Atmosphere).
* **Karakteristike:** 13 spektralnih kanala (primarno NIR i Red za izračun NDVI indeksa).

* **Izvor:** [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) (Misija Sentinel-2A).
* **Službeni portal:** [dataspace.copernicus.eu](https://dataspace.copernicus.eu/)
* **Metadata Search:** STAC API (`stac.dataspace.copernicus.eu`)
* **Product Catalog:** OData API (`catalogue.dataspace.copernicus.eu`)
* **Data Stream:** S3 Cloud Storage (`eodata.dataspace.copernicus.eu`)

* **Dataset Link:** [https://fotoklubzagreb-my.sharepoint.com/:f:/g/personal/josip_smoljic_fotoklubzagreb_hr/IgCR06dwIwWTR51OT7DRX4J3Aa1shBB-VFuw2BPHAWfuA_E?e=seMpCK] - *Sadrži pripremljene pločice (tiling) i normalizirane maske. (3GB)*

* **Opis izgradnje:** Podaci su procesirani i očišćeni od naoblake (cloud masking) te izrezani na dimenzije pogodne za trening UNet modela.

## 3. Arhitektura Modela i Pristup
Model se temelji na **MasterUNet** arhitekturi (ResNet-UNet hibrid):
* **Encoder:** Koristi ResNet bazu za ekstrakciju dubokih značajki urbanih tekstura.
* **Decoder:** Putem *Skip Connections* mehanizma precizno mapira granice novih građevinskih zona.
* **Logika:** Model ne predviđa samo sliku, već spektralne vrijednosti (NDVI) koje se kasnije diskretiziraju u kategorije zemljišta.

## 4. Rezultati i Evaluacija
Model je postigao visoku preciznost u prepoznavanju trendova širenja grada:
* **Accuracy:** 82% (na razini piksela)
* **Interpretacija:** Evaluacija pokazuje da sustav najtočnije predviđa širenje uz postojeće infrastrukturne čvorove (npr. rubni dijelovi Novog Zagreba i zapadni ulaz u grad).


## 5. Analitički Engine
* **Temporalna usporedba:** Vizualizacija urbanog širenja od 2016. do predviđenih projekcija za 2027. i 2050. godinu.
* **Kvantifikacija gubitka biomase:** Izračun smanjenja zelenih površina u odnosu na rast građevinskih zona.

### 6. Napredna Vizualizacija (app.py)
* **Delta Display Mode:** Inovativni prikaz koji izolira isključivo "novu urbanizaciju" (promjenu između dva vremenska razdoblja).
* **Binary Construction View:** Poseban način rada koji filtrira sve osim novih gradilišta i urbanih zona.
* **Discretization:** Kategorizacija zemljišta u intuitivne klase radi lakšeg razumijevanja za krajnje korisnike (urbaniste).
Model identificira trendove urbanizacije s visokom preciznošću, naglašavajući kritične točke gubitka zelene infrastrukture u širem području grada Zagreba.

<img width="1746" height="1039" alt="urban" src="https://github.com/user-attachments/assets/ed468e26-8138-40a4-8d9b-1bf340bb1347" />
<img width="1744" height="1039" alt="ndvi" src="https://github.com/user-attachments/assets/432c161f-1f14-469b-867e-75e7998af3cc" />

## 5. Kako pokrenuti projekt (Demo)
**Kloniranje repozitorija i pokretanje:**
   ```bash
        # Kloniranje cijelog repozitorija
        git clone https://github.com/klodovic/AI_Lipik.git

        # Ulazak u mapu
        cd AI_Lipik/Projekti/Zavrsni-rad

        # Instalacija biblioteka
        pip install -r requirements.txt

        # Pokrenite aplikaciju
        streamlit run app.py  

### Tech Stack
* **Jezik:** Python 3.x
* **ML Framework:** PyTorch / TensorFlow (MasterUNet V3)
* **Sučelje:** Streamlit (za interaktivni `app.py`)

---
*travanj 2026.*
