# Urban Growth Prediction - Zagreb 2050 
**Deep Learning sustav za simulaciju i analizu urbanizacije koristeći satelitske podatke.**

Ovaj projekt koristi napredne tehnike računalnog vida i umjetne inteligencije za praćenje transformacije grada Zagreba. Cilj je dokumentirati potiskivanje prirode pod naletom urbanizacije te predvidjeti buduće trendove širenja gradskog betona.

<a class="yt-privacy-embed" href="https://www.youtube.com/watch?v=uDxlzmlc52k" style="display:block;position:relative;width:100%;aspect-ratio:16/9;background:#000;" onclick="event.preventDefault();this.outerHTML='<iframe width=\'100%\' height=\'100%\' src=\'https://www.youtube-nocookie.com/embed/uDxlzmlc52k?autoplay=1\' title=\'YouTube video player\' frameborder=\'0\' allow=\'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\' referrerpolicy=\'strict-origin-when-cross-origin\' allowfullscreen style=\'aspect-ratio:16/9;\'></iframe>'">
  <img src="https://i.ytimg.com/vi/uDxlzmlc52k/maxresdefault.jpg" alt="Video thumbnail" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;" onerror="this.src='https://i.ytimg.com/vi/uDxlzmlc52k/hqdefault.jpg'">
  <svg style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;" viewBox="0 0 68 48">
    <path d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 0 34 0S12.21.13 6.9 1.55c-2.93.78-4.63 3.26-5.42 6.19C.06 13.05 0 24 0 24s.06 10.95 1.48 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 48 34 48s21.79-.13 27.1-1.55c2.93-.78 4.64-3.26 5.42-6.19C67.94 34.95 68 24 68 24s-.06-10.95-1.48-16.26z" fill="#ff0000"/>
    <path d="M45 24L27 14v20" fill="#fff"/>
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
