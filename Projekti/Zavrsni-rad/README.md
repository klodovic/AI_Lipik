# Urban Growth Prediction - Zagreb 2050 
**Deep Learning sustav za simulaciju i analizu urbanizacije koristeći satelitske podatke.**

Ovaj projekt koristi napredne tehnike računalnog vida i umjetne inteligencije za praćenje transformacije grada Zagreba. Cilj je dokumentirati potiskivanje prirode pod naletom urbanizacije te predvidjeti buduće trendove širenja gradskog betona.

[![Video Presentation](https://i.ytimg.com/vi/uDxlzmlc52k/maxresdefault.jpg)](https://www.youtube.com/watch?v=uDxlzmlc52k)
*Kliknite na sliku iznad za pokretanje video prezentacije na YouTube-u (preporučeno: desni klik -> otvori u novoj kartici).*

## Ključne značajke

### 1. Integracija s Copernicus Programom
* **Satelitski podaci:** Automatska obrada multispektralnih snimki s misije **Sentinel-2A**.
* **Spektralna analiza:** Korištenje 13 spektralnih kanala (uključujući infracrveni spektar) za preciznu detekciju NDVI (vegetacijskog indeksa) i izgrađenih površina.
* **Procesiranje:** Korištenje **L2A (Level-2A)** podataka koji su atmosferski korigirani (Bottom-Of-Atmosphere), što osigurava znanstvenu točnost izračuna indeksa.

### 2. MasterUNet Arhitektura
* **Hibridni model:** Implementacija **ResNet-UNet** arhitekture koja kombinira duboko učenje značajki s preciznim prostornim mapiranjem.
* **Skip Connections:** Korištenje preskočnih veza za očuvanje detalja niske razine tijekom procesa dekodiranja.
* **Optimizacija:** Napredni trening kroz tisuće iteracija s Min-Max normalizacijom i dinamičkim batchingom.

### 3. Napredna Vizualizacija (app.py)
* **Delta Display Mode:** Inovativni prikaz koji izolira isključivo "novu urbanizaciju" (promjenu između dva vremenska razdoblja).
* **Binary Construction View:** Poseban način rada koji filtrira sve osim novih gradilišta i urbanih zona.
* **Discretization:** Kategorizacija zemljišta u intuitivne klase radi lakšeg razumijevanja za krajnje korisnike (urbaniste).

### 4. Analitički Engine
* **Temporalna usporedba:** Vizualizacija urbanog širenja od 2016. do predviđenih projekcija za 2027. i 2050. godinu.
* **Kvantifikacija gubitka biomase:** Izračun smanjenja zelenih površina u odnosu na rast građevinskih zona.

## Tehnologije i Izvori Podataka

### Dataset i API
Glavni izvor podataka je **Copernicus Data Space Ecosystem (CDSE)**. Sustav koristi automatizirane skripte za dohvaćanje podataka putem:
* **Službeni portal:** [dataspace.copernicus.eu](https://dataspace.copernicus.eu/)
* **Metadata Search:** STAC API (`stac.dataspace.copernicus.eu`)
* **Product Catalog:** OData API (`catalogue.dataspace.copernicus.eu`)
* **Data Stream:** S3 Cloud Storage (`eodata.dataspace.copernicus.eu`)

### Tech Stack
* **Jezik:** Python 3.x
* **ML Framework:** PyTorch / TensorFlow (MasterUNet V3)
* **Sučelje:** Streamlit (za interaktivni `app.py`)

## Rezultati
Model identificira trendove urbanizacije s visokom preciznošću, naglašavajući kritične točke gubitka zelene infrastrukture u širem području grada Zagreba.

<img width="1746" height="1039" alt="urban" src="https://github.com/user-attachments/assets/ed468e26-8138-40a4-8d9b-1bf340bb1347" />
<img width="1744" height="1039" alt="ndvi" src="https://github.com/user-attachments/assets/432c161f-1f14-469b-867e-75e7998af3cc" />

---
*travanj 2026.*