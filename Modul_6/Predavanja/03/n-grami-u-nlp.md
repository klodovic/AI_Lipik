# N-grami u obradi prirodnog jezika (NLP)

N-gram je uzastopni niz od 'N' elemenata (riječi ili znakova) iz teksta ili govora. Elementi mogu biti slova, riječi ili bazni parovi, ovisno o primjeni. Vrijednost 'N' određuje red N-grama. To je temeljni koncept koji se koristi u raznim NLP zadacima poput jezičnog modeliranja, klasifikacije teksta, strojnog prevođenja i slično.

## Vrste N-grama

N-grami mogu biti različitih tipova ovisno o vrijednosti 'N':

- **Unigrami (1-grami)** — pojedinačne riječi
- **Bigrami (2-grami)** — parovi uzastopnih riječi
- **Trigrami (3-grami)** — trojke uzastopnih riječi

## Primjene N-grama u NLP-u

- **Hvatanje konteksta i semantike** — N-grami pomažu razumjeti kako riječi funkcioniraju zajedno u rečenici. Analizom malih kombinacija riječi pružaju uvid u značenje i tok jezika, čineći interpretaciju teksta preciznijom.
- **Poboljšanje jezičnih modela** — U alatima poput sustava za prevođenje ili glasovnih asistenata, N-grami pomažu predvidjeti sljedeću riječ u rečenici, što dovodi do prirodnijih i točnijih odgovora.
- **Predviđanje teksta** — Široko se koriste u prediktivnom tipkanju. Analizom već upisanih riječi pomažu predložiti sljedeću riječ, čineći pisanje bržim i intuitivnijim.
- **Pretraživanje informacija** — Pomažu tražilicama pronaći i rangirati dokumente prepoznavanjem važnih uzoraka riječi, čime pretraživači postaju učinkovitiji u isporuci relevantnih rezultata.

## Implementacija N-grama

- `text.split()` — razdvaja tekst u listu riječi (tokena)
- `[tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]` — generira N-grame stvaranjem n-torki uzastopnih riječi
- `return ngrams` — vraća listu generiranih N-grama

```python
def generate_ngrams(text, n):
    tokens = text.split()
    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    return ngrams


text = "Geeks for Geeks Community"

unigrams = generate_ngrams(text, 1)
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)

print("Unigrami:", unigrams)
print("Bigrami:", bigrams)
print("Trigrami:", trigrams)
```

**Izlaz:**

```
Unigrami: [('Geeks',), ('for',), ('Geeks',), ('Community',)]
Bigrami: [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
Trigrami: [('Geeks', 'for', 'Geeks'), ('for', 'Geeks', 'Community')]
```

## Laplaceovo izglađivanje za N-grame

Jedan od glavnih izazova pri radu s N-gramima je **rijetka zastupljenost podataka** (*data sparsity*), posebno kod N-grama višeg reda poput 4-grama ili 5-grama. Kako vrijednost N raste, broj mogućih N-grama eksponencijalno raste, a mnogi se možda neće pojaviti u podacima za treniranje, što rezultira nultim vjerojatnostima za neviđene sekvence.

Za rješavanje ovog problema koristi se **Laplaceovo izglađivanje** (poznato i kao aditivno izglađivanje). Ono dodaje konstantu (obično 1) svakom broju pojavljivanja, osiguravajući da nijedan N-gram nema nultu vjerojatnost, čak i ako nije viđen u skupu za treniranje.

### Formula

```
Izglađeni broj = (broj + 1) / (ukupni N-grami + veličina vokabulara)
```

Gdje je:

- **broj** — frekvencija određenog N-grama u skupu podataka
- **ukupni N-grami** — broj N-grama u skupu podataka
- **veličina vokabulara** — ukupan broj jedinstvenih riječi

### Primjer koda

```python
from collections import Counter


def laplace_smoothing(ngrams, vocab_size):
    ngram_counts = Counter(ngrams)
    smoothed_ngrams = {ngram: (count + 1) / (len(ngrams) + vocab_size)
                       for ngram, count in ngram_counts.items()}
    return smoothed_ngrams


ngrams = [('Geeks', 'for'), ('for', 'Geeks'), ('Geeks', 'Community')]
vocab_size = 5

smoothed_ngrams = laplace_smoothing(ngrams, vocab_size)
print("Izglađeni N-grami:", smoothed_ngrams)
```

**Izlaz:**

```
Izglađeni N-grami: {('Geeks', 'for'): 0.25, ('for', 'Geeks'): 0.25, ('Geeks', 'Community'): 0.25}
```

## Usporedba: N-grami naspram drugih NLP modela

| Aspekt | N-gram modeli | HMM (Skriveni Markovljevi modeli) | RNN (Rekurentne neuronske mreže) | Modeli bazirani na Transformerima |
|---|---|---|---|---|
| Kontekstni prozor | Fiksne veličine (N riječi) | Ograničen, ovisi o prijelazima stanja | Fleksibilan (pamti prethodna stanja) | Vrlo velik (globalna pažnja) |
| Semantičko razumijevanje | Vrlo ograničeno | Slabo | Umjereno | Dobro |
| Učinkovitost s podacima | Dobra s malo podataka | Dobra s malo podataka | Treba više podataka | Treba veliku količinu podataka |
| Brzina i jednostavnost | Brzo i jednostavno | Umjereno | Sporije od N-grama | Sporo |
| Interpretabilnost | Lako razumljivo | Umjereno | Teško za interpretirati | Crna kutija |
| Primjene | Osnovni NLP zadaci | POS označavanje, označavanje sekvenci | Jezično modeliranje, označavanje sekvenci | Prevođenje, sažimanje, pitanja i odgovori |

## Primjene N-grama

- **Jezično modeliranje** — Predviđaju sljedeću riječ u rečenici na temelju prethodnih riječi, pomažući generirati relevantan tekst u zadacima poput generiranja teksta, chatbotova i sustava automatskog dovršavanja.
- **Predviđanje teksta** — U prediktivnom tipkanju predlažu sljedeću riječ na temelju nedavnog unosa, poboljšavajući brzinu tipkanja i korisničko iskustvo u aplikacijama poput mobilnih tipkovnica.
- **Klasifikacija sentimenta i teksta** — N-grami hvataju sekvence riječi za klasifikaciju teksta u kategorije ili sentimente, olakšavajući identifikaciju tona i tema.
- **Detekcija plagijarizma** — Usporedbom N-grama u dokumentima sustavi mogu uočiti slične uzorke, pomažući u otkrivanju kopiranog ili preformuliranog sadržaja.
- **Prepoznavanje govora** — U sustavima za pretvorbu govora u tekst predviđaju sljedeću riječ, čime poboljšavaju točnost transkripcije s kontekstualno ispravnim sekvencama.

## Prednosti N-grama u NLP-u

- **Jednostavnost implementacije** — Lako su razumljivi i zahtijevaju minimalne računalne resurse. Pogodni su za početno modeliranje i brzo prototipiranje.
- **Nizak računalni teret** — U usporedbi s neuronskim pristupima, računalno su lagani i lako skalabilni, čineći ih pogodnima za sustave s ograničenom procesorskom snagom.
- **Očuvanje lokalnog reda riječi** — Hvataju kratkoročne ovisnosti između riječi očuvanjem njihovog neposrednog redoslijeda, što je korisno za modeliranje sintaktičkih uzoraka poput negacije ("nije dobro") ili frazalnih konstrukcija ("New York City").
- **Solidna početna razina performansi** — Unatoč jednostavnosti, često pružaju konkurentne početne rezultate za niz zadataka uključujući klasifikaciju teksta, analizu sentimenta, pretraživanje informacija i detekciju tema.

## Izazovi i ograničenja

- **Rijetka zastupljenost podataka** — S većim N-gramima postaje manje vjerojatno pronaći ponovljene instance iste sekvence, što dovodi do rijetkih podataka.
- **Nedostatak semantičkog razumijevanja** — Iako su N-grami dobri u prepoznavanju uzoraka, nemaju razumijevanje konteksta izvan sekvenci na kojima su trenirani.
- **Nedostatak konteksta na daljinu** — Uzimaju u obzir samo obližnje riječi i ignoriraju šire značenje rečenice.

---

*Izvor: [GeeksforGeeks — N-gram in NLP](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)*
