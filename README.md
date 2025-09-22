
    <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Niki.ai-logo.svg" alt="AI logo">
    <h1>AI_Lipik</h1>
    <p><em>Stručnjak/inja za umjetnu inteligenciju</em></p>

    <h2>Sadržaj</h2>
    <ul>
      <li><a href="#modul-2---projektni-zadatak">Modul 2 - projektni zadatak</a></li>
      <li><a href="#modul-3---strojno-ucenje">Modul 3 - Strojno učenje</a>
        <ul>
          <li><a href="#01-uvodno-predavanje">01. Uvodno predavanje</a></li>
          <li><a href="#02-ponavljanje-matematike">02. Ponavljanje matematike</a></li>
          <li><a href="#03-klasifikacija-k-nn-nb">03. Klasifikacija (k-NN, NB)</a></li>
          <li><a href="#04-regresija-k-nn-linearna">04. Regresija (k-NN, linearna)</a></li>
          <li><a href="#05-evaluacija">05. Evaluacija</a></li>
          <li><a href="#06-pogreska-klasifikatora">06. Pogreška klasifikatora</a></li>
          <li><a href="#07-procjena-regresora">07. Procjena regresora</a></li>
        </ul>
      </li>
    </ul>

    <h2 id="modul-2---projektni-zadatak">Modul 2 - projektni zadatak</h2>
    <ul>
      <li><strong>Učitati dataset i osnovna analiza</strong> <em>(2 boda)</em>
        <ul>
          <li>Prikazati osnovne informacije pomoću <code>head()</code>, <code>describe()</code> i <code>info()</code>.</li>
          <li>Dodati komentare: npr. raspon starosti, sumnjive vrijednosti, očekivani/neočekivani podaci itd.</li>
        </ul>
      </li>
      <li><strong>Upoznati se s kategoričkim varijablama</strong> <em>(2 boda)</em>
        <ul>
          <li>Ispitati koliko podataka ima unutar svake kategorije, npr. u koloni <code>Spol</code>.</li>
        </ul>
      </li>
      <li><strong>Čišćenje podataka</strong>
        <ul>
          <li><strong>Srediti duplikate</strong> <em>(2 boda)</em></li>
          <li><strong>Srediti missing values</strong> <em>(4 boda)</em></li>
          <li><strong>Srediti outliere</strong> <em>(4 boda)</em></li>
          <li><strong>Srediti krive upise</strong> <em>(4 boda)</em>
            <ul>
              <li>Provjeriti npr. na koliko načina je napisan spol ("Muško", "musko", "M", itd.).</li>
            </ul>
          </li>
        </ul>
      </li>
      <li><strong>Otkriti veze među podacima</strong> <em>(6 bodova)</em>
        <ul>
          <li>Primijeniti korelaciju, grafičke prikaze, grupiranja i druge metode za otkrivanje odnosa među varijablama.</li>
        </ul>
      </li>
      <li><strong>Odrediti koje varijable ostaju u datasetu, a koje se miču</strong> <em>(4 boda)</em>
        <ul>
          <li>Objasniti razloge uklanjanja varijabli: npr. niska varijanca, visoka korelacija s drugima, neinformativnost; temeljeno na statistikama i/ili domain knowledge.</li>
        </ul>
      </li>
    </ul>

    <h2 id="modul-3---strojno-ucenje">Modul 3 - Strojno učenje</h2>

    <h3 id="01-uvodno-predavanje">01. Uvodno predavanje</h3>
    <ul>
      <li>Supervised vs Unsupervised Learning<br>
        <a href="https://www.youtube.com/watch?v=SYPejHY9WV8">https://www.youtube.com/watch?v=SYPejHY9WV8</a>
      </li>
    </ul>

    <h3 id="02-ponavljanje-matematike">02. Ponavljanje matematike</h3>
    <ul>
      <li>What Is Scikit-Learn ?<br>
        <a href="https://www.youtube.com/watch?v=7z8-QWlbmoo">https://www.youtube.com/watch?v=7z8-QWlbmoo</a>
      </li>
    </ul>

    <h3 id="03-klasifikacija-k-nn-nb">03. Klasifikacija (k-NN, NB)</h3>
    <ul>
      <li>KNN Algorithm in Machine Learning<br>
        <a href="https://www.youtube.com/watch?v=TN_iv1ToxmI">https://www.youtube.com/watch?v=TN_iv1ToxmI</a>
      </li>
      <li>Naive Bayes Algorithm in Machine Learning<br>
        <a href="https://www.youtube.com/watch?v=EK9uEfR53n4">https://www.youtube.com/watch?v=EK9uEfR53n4</a>
      </li>
    </ul>

    <h3 id="04-regresija-k-nn-linearna">04. Regresija (k-NN, linearna)</h3>
    <ul>
      <li>KNN machine learning model for regression<br>
        <a href="https://www.youtube.com/watch?v=ywbVXMuhDhk">https://www.youtube.com/watch?v=ywbVXMuhDhk</a>
      </li>
      <li>Linear Regression Algorithm<br>
        <a href="https://www.youtube.com/watch?v=1aktNYADxdc">https://www.youtube.com/watch?v=1aktNYADxdc</a>
      </li>
    </ul>

    <h3 id="05-evaluacija">05. Evaluacija</h3>
    <ul>
      <li>Bias variance trade off and overfitting<br>
        <a href="https://www.youtube.com/watch?v=EEHhGRq-r1c">https://www.youtube.com/watch?v=EEHhGRq-r1c</a>
      </li>
      <li>Cross validation<br>
        <a href="https://www.youtube.com/watch?v=1aktNYADxdc">https://www.youtube.com/watch?v=1aktNYADxdc</a>
      </li>
    </ul>

    <h3 id="06-pogreska-klasifikatora">06. Pogreška klasifikatora</h3>
    <ul>
      <li>
        Gist: <a href="https://gist.github.com/kdokic1971/ffa9193934236af91cd79cabdc5f36f5" target="_blank" rel="noopener">https://gist.github.com/kdokic1971/ffa9193934236af91cd79cabdc5f36f5</a>
      </li>
    </ul>

    <h4>DODATNI MATERIJALI</h4>
    <ul>
      <li>ROC and AUC, Clearly Explained!<br>
        <a href="https://www.youtube.com/watch?v=4jRBRDbJemM">https://www.youtube.com/watch?v=4jRBRDbJemM</a>
      </li>
    </ul>

    <h3 id="07-procjena-regresora">07. Procjena regresora</h3>
    <ul>
      <li>Gist 1: <a href="https://gist.github.com/kdokic1971/e7d7dd04d3015de488c370e193db6c2b" target="_blank" rel="noopener">https://gist.github.com/kdokic1971/e7d7dd04d3015de488c370e193db6c2b</a></li>
      <li>Gist 2: <a href="https://gist.github.com/kdokic1971/3a773ab78c140b35e060a95bae683c33" target="_blank" rel="noopener">https://gist.github.com/kdokic1971/3a773ab78c140b35e060a95bae683c33</a></li>
    </ul>
