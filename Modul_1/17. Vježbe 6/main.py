

'''
1.	Napišite program koji koristi for petlju za ispis pozdrava svakoj osobi u zadanoj listi imena.
    a.	Zadana lista: imena = ["Ana", "Marko", "Iva", "Petar"]
    b.	Što treba ispisati: Za svako ime u listi, ispišite poruku poput: "Pozdrav, Ana!"
'''
print("Zadatak 1")
imena = ["Ana", "Marko", "Iva", "Petar"]
for ime in imena:
    print(f'Pozdrav, {ime}.')
print()


'''
2.	Napišite program koji koristi for petlju i funkciju range() za ispis brojeva od 1 do 10 (uključujući 10).
'''
print("Zadatak 2")
for i in range(1,11):
    print(i)
print()


'''
3.	Napišite program koji koristi for petlju za prolazak kroz svaki znak u zadanoj riječi i ispisuje svaki znak na novom retku.
    a.	Zadana riječ: rijec = "Python"
'''
print("Zadatak 3")
text = "Python"
for t in text:
    print(t)
print()


'''
4.	Napišite program koji koristi for petlju i funkciju range() za prolazak kroz brojeve od 1 do 20. Unutar petlje, 
    	koristite if izraz da provjerite je li broj paran, i ispišite ga samo ako jest.
'''
print("Zadatak 4")
for i in range(1, 21):
    if i%2 == 0:
        print(f'Broj {i} je paran.')
print()


'''
5.	Napišite program koji izračunava prosjek ocjena iz zadane liste.
    a.	Zadana lista ocjena: ocjene = [5, 4, 3, 5, 4, 2, 5, 5, 3, 4]
    b.	Upute: 
    c.	Inicijalizirajte varijablu ukupni_zbroj_ocjena na 0.
    d.	Inicijalizirajte varijablu broj_ocjena na 0.
    e.	Koristite for petlju za prolazak kroz svaku ocjenu u listi ocjene.
    f.	Unutar petlje, dodajte svaku ocjenu u ukupni_zbroj_ocjena i povećajte broj_ocjena za 1.
    g.	Nakon petlje, izračunajte prosjek tako da ukupni_zbroj_ocjena podijelite s broj_ocjena.
    h.	Ispišite izračunati prosjek.
'''
print("Zadatak 5")
ocjene = [5, 4, 3, 5, 4, 2, 5, 5, 3, 4]
ukupni_zbroj_ocjena = 0
broj_ocjena = 0

for ocjena in ocjene:
    ukupni_zbroj_ocjena =+ ocjena
    broj_ocjena =+1
print(f'Prosjek ocjena: {ukupni_zbroj_ocjena / broj_ocjena}')
print()


'''
6.	Napišite program koji iz zadanog rječnika proizvoda izdvaja samo nazive onih proizvoda čija je cijena veća od određene vrijednosti.
    a.	Koristite sljedeći rječnik gdje su ključevi (keys) nazivi proizvoda (stringovi), a vrijednosti (values) su njihove cijene (brojevi).
    b.	proizvodi_i_cijene = { "Laptop": 1200, "Miš": 25, "Tipkovnica": 75, "Monitor": 300, "Web kamera": 50, "Printer": 150, "Slušalice": 40 }
    c.	Zadana granična cijena iznosi 100 i nalazi se u posebnoj varijabli
    d.	Nazive proizvoda (ključeve) koji zadovoljavaju uvjet da su veći od 100 pohranite u novu listu
'''
print("Zadatak 6")
izdvojene_cijene = []
granicna_cijena = 100
proizvodi_i_cijene = { "Laptop": 1200, "Miš": 25, "Tipkovnica": 75, "Monitor": 300, "Web kamera": 50, "Printer": 150, "Slušalice": 40 }

for cijena in proizvodi_i_cijene.values():
    if cijena > granicna_cijena:
        izdvojene_cijene.append(cijena)
print(f'Izdvojne cijene iznad 100: {izdvojene_cijene}')
print()


'''
7.	Pronalaženje najduže riječi - napišite program koji u zadanoj listi riječi pronalazi i ispisuje najdužu riječ.
    a.	Zadana lista riječi: rijeci = ["jabuka", "banana", "programiranje", "stol", "računalo", "kratko"]
    b.	Upute:
    c.	Inicijalizirajte varijablu najduza_rijec na prazan string "".
    d.	Koristite for petlju za prolazak kroz svaku riječ u listi riječi.
    e.	Unutar petlje, usporedite duljinu trenutne riječi s duljinom riječi pohranjene u najduza_rijec.
    f.	Ako je trenutna riječ duža od najduza_rijec, ažurirajte najduza_rijec s trenutnom riječi.
    g.	Nakon petlje, ispišite pronađenu najduza_rijec.
'''
print("Zadatak 7")
najdulja_rijec = ""
rijeci = ["jabuka", "banana", "programiranje", "stol", "računalo", "kratko"]

for rijec in rijeci:
    if len(rijec) > len(najdulja_rijec):
        najdulja_rijec = rijec
print(f'Najdulja rijec u listi je: {najdulja_rijec}')
print()


'''
8.	Analiza brojeva u listi - Napišite program koji analizira zadanu listu cijelih brojeva i prebrojava koliko je u njoj pozitivnih brojeva, 
    koliko negativnih brojeva i koliko nula.
    a.	Koristite sljedeću listu: brojevi = [5, -3, 0, 10, -8, 0, 15, -1, 7]

'''
print("Zadatak 8")
brojevi = [5, -3, 0, 10, -8, 0, 15, -1, 7]
pozitivni = 0
negativni = 0
nule = 0
for broj in brojevi:
    if broj > 0:
        pozitivni += 1
    elif broj < 0:
        negativni += 1
    else:
        nule += 1
print(f"Pozitivnih brojevi: {pozitivni}, negativnih brojevi: {negativni}, nule {nule}.")
print()


'''
9.	Cilj projekta: Napišite program koji će pronaći sve moguće parove brojeva, gdje je jedan broj iz prve liste, 
    a drugi broj iz druge liste, tako da njihov zbroj bude jednak zadanoj ciljanoj vrijednosti.
    a.	Koristite ove liste:
    i.	lista1 = [1, 2, 3, 4, 5]
    ii.	lista2 = [6, 7, 8, 9, 10]
    b.	Definirajte varijablu ciljani_zbroj = 10.
'''
print("Zadatak 9")
ciljani_zbroj = 10
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

for broj1 in lista1:
    for broj2 in lista2:
        if broj1 + broj2 == ciljani_zbroj:
            print(f"{broj1} + {broj2} = {ciljani_zbroj}")























































