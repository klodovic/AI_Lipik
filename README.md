# ![Materials](https://img.shields.io/badge/Materials-Available-brightgreen) ![Content](https://img.shields.io/badge/Content-Videos%2FText%2FExamples-blue) ![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey)

<a title="United Blasters, CC BY 4.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:AI_logo_by_United_Blasters.png">
  <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/AI_logo_by_United_Blasters.png/256px-AI_logo_by_United_Blasters.png" alt="AI logo by United Blasters">
</a>

# AI_Lipik
*Stručnjak/inja za umjetnu inteligenciju*

---

## Sadržaj
- [Modul 2 - projektni zadatak](#modul-2---projektni-zadatak)
- [Modul 3 - Strojno učenje](#modul-3---strojno-ucenje)
  - [01. Uvodno predavanje](#01-uvodno-predavanje)
  - [02. Ponavljanje matematike](#02-ponavljanje-matematike)
  - [03. Klasifikacija (k-NN, NB)](#03-klasifikacija-k-nn-nb)
  - [04. Regresija (k-NN, linearna)](#04-regresija-k-nn-linearna)
  - [05. Evaluacija](#05-evaluacija)
  - [06. Pogreška klasifikatora](#06-pogreska-klasifikatora)
  - [07. Procjena regresora](#07-procjena-regresora)
  - [08. Nove metode klasifikacije](#08-nove-metode-klasifikacije)
  - [09. Nove metode regresije](#09-nove-metode-regresije)
  - [10. Manipuliranje značajkama](#10-manipuliranje-znacajkama)
  - [11. Podešavanje hiperparametara i cjevovoda](#11-podesavanje-hiperparametara-i-cjevovoda)
  - [12. Kombiniranje modela](#12-kombiniranje-modela)
  - [13. (prazno)](#13)
  - [14. Upravljanje svojstvima u posebnim područjima](#14-upravljanje-svojstvima-u-posebnim-podrucjima)
  - [15. Ostale teme](#15-ostale-teme)
  - [16. Nenadzirano učenje (1. dio)](#16-nenadzirano-ucenje-1-dio)
  - [17. Nenadzirano učenje (2. dio)](#17-nenadzirano-ucenje-2-dio)
  - [18. Objašnjivo strojno učenje (1. dio)](#18-objasnjivo-strojno-ucenje-1-dio)
  - [19. Objašnjivo strojno učenje (2. dio)](#19-objasnjivo-strojno-ucenje-2-dio)
  - [20. Provjera znanja](#20-provjera-znanja)

---

## Modul 2 - projektni zadatak

- Učitati dataset i osnovna analiza  
  - Prikazati osnovne informacije pomoću `head()`, `describe()` i `info()`.  
  - Dodati komentare: raspon starosti, sumnjive vrijednosti, očekivani/neočekivani podaci.

- Upoznati se s kategoričkim varijablama  
  - Ispitati koliko podataka ima unutar svake kategorije, npr. u koloni `Spol`.

- Čišćenje podataka  
  - Srediti duplikate  
  - Srediti missing values  
  - Srediti outliere  
  - Srediti krive upise (npr. na koliko načina je napisan spol: "Muško", "musko", "M", itd.)

- Otkriti veze među podacima  
  - Primijeniti korelaciju, grafičke prikaze, grupiranja i druge metode

- Odrediti koje varijable ostaju u datasetu, a koje se miču  
  - Razlozi uklanjanja: niska varijanca, visoka korelacija s drugima, neinformativnost; temeljeno na statistikama i/ili domain knowledge.

---

## Modul 3 - Strojno učenje

### 01. Uvodno predavanje

Supervised vs Unsupervised Learning  
[Video](https://www.youtube.com/watch?v=SYPejHY9WV8)

---

### 02. Ponavljanje matematike

What Is Scikit-Learn?  
[Video](https://www.youtube.com/watch?v=7z8-QWlbmoo)

---

### 03. Klasifikacija (k-NN, NB)

KNN Algorithm in Machine Learning  
[Video](https://www.youtube.com/watch?v=TN_iv1ToxmI)

Naive Bayes Algorithm in Machine Learning  
[Video](https://www.youtube.com/watch?v=EK9uEfR53n4)

---

### 04. Regresija (k-NN, linearna)

KNN machine learning model for regression  
[Video](https://www.youtube.com/watch?v=ywbVXMuhDhk)

Linear Regression Algorithm  
[Video](https://www.youtube.com/watch?v=1aktNYADxdc)

---

### 05. Evaluacija

Bias variance trade off and overfitting  
[Video](https://www.youtube.com/watch?v=EEHhGRq-r1c)

Cross validation  
[Video](https://www.youtube.com/watch?v=1aktNYADxdc)

---

### 06. Pogreška klasifikatora

Matrica konfuzije za otkrivene pragove  
[Gist link](https://gist.github.com/kdokic1971/ffa9193934236af91cd79cabdc5f36f5)

Dodatni materijali:  
ROC and AUC, Clearly Explained!  
[Video](https://www.youtube.com/watch?v=4jRBRDbJemM)

---

### 07. Procjena regresora

Crtanje grešaka  
[Gist link](https://gist.github.com/kdokic1971/e7d7dd04d3015de488c370e193db6c2b)

Regression residuals  
[Gist link](https://gist.github.com/kdokic1971/3a773ab78c140b35e060a95bae683c33)

Evaluacija regresora bolja (1. dio)  
[Gist link](https://gist.github.com/kdokic1971/b3fe1fefb9121973ae66bed7639d95bf)

Evaluacija regresora bolja (2. dio)  
[Gist link](https://gist.github.com/kdokic1971/77a49160506a31ea7a5f75d2bf4f1810)

Evaluacija regresora bolja (3. dio)  
[Gist link](https://gist.github.com/kdokic1971/31842570ab5af6a2995754217c595e3b)

---

### 08. Nove metode klasifikacije

Plot-boundary  
[Gist link](https://gist.github.com/kdokic1971/f74dcafdb4f49bdcdbe9992354856724)

Dodatni Gist  
[Gist link](https://gist.github.com/kdokic1971/5e1d371a55d36fd9d967003f5feb4981)

Dodatni materijali:  
Decision Tree Machine Learning  
[Video](https://www.youtube.com/watch?v=hChoEjNlYnc)

SVM Algorithm in Machine Learning  
[Video](https://www.youtube.com/watch?v=1YW76WISm04)

Logistic Regression in Machine Learning  
[Video](https://www.youtube.com/watch?v=qfHLY0bA-Gc)

PINETOOLS - besplatni online alati za konverziju slika  
[Link](https://pinetools.com/c-images/)


### 09. Nove metode regresije

Dodatni materijali:  
Ridge regression  
[Video](https://www.youtube.com/watch?v=cR9vXkS4ulU)

LASSO regression  
[Video](https://www.youtube.com/watch?v=t_1ZSWGDkX4)

Support Vector Machines Regression
[Video](https://www.youtube.com/watch?v=EESZtSOdhEQ)

Decision Tree Regression and classification models  
[Video](https://www.youtube.com/watch?v=1I5MBdkpWgo)

### 10. Manipuliranje značajkama

*(materijali nedostaju)*

### 11. Podešavanje hiperparametara i cjevovoda

*(materijali nedostaju)*

### 12. Kombiniranje modela

*(materijali nedostaju)*

### 13.

*(materijali nedostaju)*

### 14. Upravljanje svojstvima u posebnim područjima

*(materijali nedostaju)*

### 15. Ostale teme

*(materijali nedostaju)*

### 16. Nenadzirano učenje (1. dio)

*(materijali nedostaju)*

---

