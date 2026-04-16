# Urban Growth Prediction - Zagreb 2050 
**Deep Learning sustav za simulaciju i analizu urbanizacije koristeći satelitske podatke.**

Ovaj projekt koristi napredne tehnike računalnog vida i umjetne inteligencije za praćenje transformacije grada Zagreba. Cilj je dokumentirati potiskivanje prirode pod naletom urbanizacije te predvidjeti buduće trendove širenja gradskog betona.

<a class="yt-privacy-embed" href="https://www.youtube.com/watch?v=uDxlzmlc52k" style="display:block;position:relative;width:100%;aspect-ratio:16/9;background:#000;" onclick="event.preventDefault();this.outerHTML='<iframe width=\'100%\' height=\'100%\' src=\'https://www.youtube-nocookie.com/embed/uDxlzmlc52k?autoplay=1\' title=\'YouTube video player\' frameborder=\'0\' allow=\'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\' referrerpolicy=\'strict-origin-when-cross-origin\' allowfullscreen style=\'aspect-ratio:16/9;\'></iframe>'">
  <img src="https://i.ytimg.com/vi/uDxlzmlc52k/maxresdefault.jpg" alt="Video thumbnail" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;" onerror="this.src='https://i.ytimg.com/vi/uDxlzmlc52k/hqdefault.jpg'">
  <svg style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:68px;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.5));" viewBox="0 0 68 68">
    <path d="M20 12 L56 34 L20 56 Z" fill="#ff0000"/>
  </svg>
</a>

## Ključni Featurei (Značajke)

### 1. Integracija s Copernicus Programom
* **Satelitski podaci:** Automatska obrada multispektralnih snimki s misije **Sentinel-2A**.
* **Spektralna analiza:** Korištenje 13 spektralnih kanala (uključujući infracrveni spektar) za preciznu detekciju NDVI (vegetacijskog indeksa) i izgrađenih površina.

### 2. MasterUNet V3 Arhitektura
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

## Tehnologije
* **Jezik:** Python 3.x
* **ML Framework:** PyTorch / TensorFlow (MasterUNet V3)
* **GIS Alati:** GDAL, Rasterio, Affine
* **Sučelje:** Streamlit (za interaktivni `app.py`)
* **Podaci:** ESA Copernicus Open Access Hub (Sentinel-2A)

## Rezultati
Model identificira trendove urbanizacije s visokom preciznošću, naglašavajući kritične točke gubitka zelene infrastrukture u širem području grada Zagreba.

---
*travanj 2026.*
