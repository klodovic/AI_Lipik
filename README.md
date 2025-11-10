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
  - [13. (Modeli koji za nas upravljaju značajkama (SVM, PCA))](#13-Modeli-koji-za-nas-upravljaju-značajkama-SVM,PCA)
  - [14. Objašnjiva umjetna inteligencija](#14-Objašnjiva-umjetna-inteligencija)
  - [15. Nenadzirano učenje (k-means)](#15-Nenadzirano-učenje-(k-means))
  - [16. Nenadzirano učenje](#16-Nenadzirano-učenje)

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

---

### 09. Nove metode regresije

Dodatni materijali:  
Regularization in machine learning | L1 and L2 Regularization | Lasso and Ridge Regression  
[Video](https://www.youtube.com/watch?v=cR9vXkS4ulU)

Ridge regression  
[Video](https://www.youtube.com/watch?v=7XvBwQeT9OI)

LASSO regression  
[Video](https://www.youtube.com/watch?v=t_1ZSWGDkX4)

Support Vector Machines regression  
[Video](https://www.youtube.com/watch?v=EESZtSOdhEQ)

Decision Tree Regression and classification models  
[Video](https://www.youtube.com/watch?v=1I5MBdkpWgo)

---

### 10. Manipuliranje značajkama

Dodatni materijali:  
Feature scaling in machine learning  
[Video](https://www.youtube.com/watch?v=yXAyrWyH5Hg)

Machine Learning Tutorial Python - 6: Dummy Variables & One Hot Encoding  
[Video](https://www.youtube.com/watch?v=9yl6-HEY7_s)

---

### 11. Podešavanje hiperparametara i cjevovoda

Dodatni Gist  
[Gist link](https://gist.github.com/kdokic1971/251fd53c322de4b4e05810e41d85a23a)

Dodatni materijali:  

GridSearchCV | Grid Search - Hyper Parameter Tuning  
[Video](https://www.youtube.com/watch?v=csae_xWc1kw)

Machine Learning Tutorial Python - 16: Hyper parameter Tuning (GridSearchCV)  
[Video](https://www.youtube.com/watch?v=HdlDYng8g9s)

---

### 12. Kombiniranje modela

Tree based ensemble methods in machine learning  
[Video](https://www.youtube.com/watch?v=Luaqst5JM7g)

Random Forest pros and cons  
[Video](https://www.youtube.com/watch?v=YJcv5hWoGSI)

Ensemble Learning in Machine Learning  
[Video](https://www.youtube.com/watch?v=F6rrzUnz9hw)

Random Forest Explained  
[Video](https://www.youtube.com/watch?v=vdfvQTi65og)

AdaBoost Algorithm In Machine Learning - Theory  
[Video](https://www.youtube.com/watch?v=RzmJ1qaCZ4w)

AdaBoost Algorithm Python Implementation  
[Video](https://www.youtube.com/watch?v=O7J9Dl1cWmM)

Boosting algorithms in machine learning (AdaBoost, GBM, XGBoost)  
[Video](https://www.youtube.com/watch?v=D9A8zIiJSAo)

---

### 13. Modeli koji za nas upravljaju značajkama (SVM, PCA)

GIST_LINK_13a  
[Gist](https://gist.github.com/kdokic1971/74ffcd0311f64358bb5b71b8722baa22)

GIST_LINK_13b  
[Gist](https://gist.github.com/kdokic1971/8524daf58786d5587bb49ea9307cba51)

Kako SVM koristi kernal trik za razdvajanje linearno nedjeljivih klasa?  
[Video](https://www.loom.com/share/f16f044984f749b191719e4830f0ceae)

---

### 14. Objašnjiva umjetna inteligencija

Dodatni materijali:  

Introduction to Explainable AI  
[Video](https://www.youtube.com/watch?v=McviMUYiG9s)

---

### 15. Nenadzirano učenje (k-means)

Povećavanje broja klastera i prikaz grafa lakta  
[Video](https://moodle.srce.hr/2025-2026/mod/page/view.php?id=5115810)

GIST 14 - metoda lakta  
[Gist](https://gist.github.com/kdokic1971/df670dba1a5106248295eb881d09e48c)

---

### 16. Nenadzirano učenje

Mastering Clustering in ML: K-Means, K-Modes, K-Prototypes & Hierarchical Methods  
[Video](https://www.youtube.com/watch?v=CvskWkAkeLM)  

Mastering Clustering techniques using Sklearn (Kmeans, Hierarchical) - 1. dio  
[Video](https://www.youtube.com/watch?v=Q-FdHb-ZslQ)  

Mastering Clustering with PyCaret - K-Modes & K-Prototypes Unveiled - 2. dio  
[Video](https://www.youtube.com/watch?v=iMP8k1fpq1s)