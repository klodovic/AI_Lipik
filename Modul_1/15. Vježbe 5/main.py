
"""
Napišite kod koji od korisnika traži da unese neki broj. Ako je broj veći od nule, ispisuje se tekst:
„Broj je pozitivan!“. Inače se ispisuje teskt: "Nije pozitivan broj!“
"""
#1
num = int(input("Unesi neki broj: "))
if num > 0:
    print(f'{num} broj je pozitivan')
else: 
    print("Nije pozitivan broj!")







"""
Napišite program koji od korisnika traži unos svoje dobi i ispisuje "Možete voziti" ako je korisnik star 18 
godina ili više, inače ispisuje "Ne možete voziti".
"""
#2
age = int(input("Koliko godina imate? "))
if age >= 18:
    print("Mozete voziti!!!")
else: 
    print("Ne mozete voziti!!!")








'''
Zatražite od korisnika da unese neki cijeli broj. Želite provjeriti je li broj paran (djeljiv s brojem 2, bez ostatka)
    a.Ako je broj paran, ispisuje se tekst: "Broj je paran!", inače se ispisuje tekst "Broj nije paran!"
    b.Hint: Koju računsku operaciju možete napraviti da utvrdite iznosi li decimalni ostatak nula (0)?
'''
#3
number = int(input("Unesi neki cijeli broj: "))
if number % 2 == 0:
    print("Broj je paran!")
else: 
    print("Broj nije paran...")








'''
Zatražite od korisnika da unese jedan od tri grada: Zagreb, Split ili Šibenik.
    a.Ovisno o unosu korisnika ispisuje se odgovarajući spomenik kulture:
        i.Za Zagreb: Crkva sv. Marka
        ii.Za Split: Crkva sv. Duje
        iii.Za Šibenik: Šibenska katedrala
        iv.U slučaju da nije unesen nijedan od ta tri grada, sipisuje se poruka o neispravnom unosu
'''
#4
town = input("Unesite jedan od tri grada - Zagreb, Split ili Sibenik: ")
if town == "Zagreb":
    print("Crkva sv. Marka")
elif town == "Split":
    print("Crkva sv. Duje")
elif town == "Sibenik":
    print("Sibenska katedrala")
else: 
    print("Neispravan unos")








'''
Zatražite od korisnika da unese neki broj. Provjerite radi li se o troznamenkastom broju ili ne te ispišite odgovarajuće poruke.
'''
#5
n = int(input("Unesi neki broj: "))
if n > 99:
    print("Broj je troznamenkast!")
else: print("Broj nije troznamenkast!")








'''
Zatražite od korisnika da unese neki broj. Odredite je li taj broj djeljiv s 2 i 3 (dijeljenjem unešenog broja s dva ili 3, nema ostatka).
    a.Ispišite odgovarajuće poruke
'''
#6
n1 = int(input("Unesi neki broj: "))
if n1 % 2 == 0 and n1 % 3 == 0:
    print("Broj je djeljiv s brojevima 2 i 3.")
elif n1 % 2 == 0:
    print("Broj je djeljiv samo s brojem 2.")
elif n1 % 3 == 0:
    print("Broj je djeljiv samo s brojem 3.")
else:
    print("Broj nije djeljiv ni s brojem 2 ni s brojem 3.")
    
    
    
    
    
    
    


'''
Zatražite od korisnika da unese dva broja, svaki pohranite u odgovarajuću varijablu. Odredite koji je broj od ta dva broja veći i 
ispišite odgovarajuće poruke.
'''
#7
num1 = int(input("Unesi prvi broj: "))
num2 = int(input("Unesi drugi broj: "))
if num1 > num2:
    print("Prvi broj je veci...")
else:
    print("Drugi broj je veci...")
    
    
    
    
    
    
    
    

'''
Zatražite od korisnika da unese neko slovo. Provjerite radi li se o samoglasniku (slova a, e, i, o, u su samoglasnici).
    a.Ispišite odgovarajuće poruke
'''
#8
letter = input("Unesite jedno slovo: ")
vowels = ["a", "e", "i", "o", "u"]

if letter.lower() in vowels:
    print("Upisali ste samoglasnik...")
else: 
    print("Upisali ste suglasnik...")









'''
Napišite program koji pomaže korisniku da provjeri da li je neka namirnica sigurna za konzumaciju na temelju popisa alergena. Korisnik će unijeti 
naziv namirnice koju planira konzumirati, a program će provjeriti da li se ta namirnica ne nalazi u popisu alergena.
    a.Koristite ovu listu: alergeni = ["jagode", "mlijeko", "kikiriki", "jaja"]
    b.Ako namirnica NIJE na popisu, ispisuje se poruka: Sigurno za konzumaciju
    c.Ako se namirnica nalazi na popisu, ispisati poruku upozorenja
'''
#9
alergeni = ["jagode", "mlijeko", "kikiriki", "jaja"]
food = input("Unesite naziv namirnice koju zelite konzumirati: ")
if food not in alergeni:
    print("Sigurno za konzumaciju.")
else:
    print("Upozorenje: namirnica nije sigurna za konzumaciju.")









'''
Napišite program koji pomaže korisniku da provjeri dostupnost smještaja na određenim destinacijama. Korisnik će unijeti naziv destinacije koju želi posjetiti, a program će provjeriti da li na toj destinaciji još uvijek ima slobodnih mjesta u hotelima.
    a.Koristite ovu listu: destinacije_sa_smjestajem = ["pariz", "rim", "barcelona", "beč", "lisabon"]
    b.Ako je korisnikova destinacija u listi, ispisuje se poruka: "Ima mjesta"
    c.Inače se ispisuje suprotna poruka, obavještava korisnika kako nažalost nema mjesta u željenoj destinaciji
'''
#10
destinacije_sa_smjestajem = ["pariz", "rim", "barcelona", "beč", "lisabon"]
destinacija = input("Unesite naziv destinacije koju zelite posjetiti: ")
if destinacija.lower() in destinacije_sa_smjestajem:
    print("Ima mjesta")
else:
    print("Nazalost nema mjesta u zeljenoj destinaciji")







'''
Zatražite od korisnika da unese jedan naziv mjeseca (tipa siječanj, veljača, ožujak itd).
    a.Ako je unio rujan, listopad ili studeni, radi se o jeseni. Ispišite jesen.
    b.Ako je unio prosinac, siječanj ili veljaču, ispišite zima
    c.Ako je unio ožujak, travanj ili svibanj, unesite proljeće
    d.Ako je unio lipanj, srpanj ili kolovoz, unesite ljeto
    e.Ako je unip nepto drugo, ispišite poruku o grešci!
'''
#11
month = input("Unesite naziv mjeseca u godini: ").lower()
jesen = ["rujan", "listopad", "studeni"]
zima = ["prosinac", "siječanj", "veljača"]
proljece = ["ožujak", "travanj", "svibanj"]
ljeto = ["lipanj", "srpanj", "kolovoz"]

if month in jesen:
    print("Jesen")
elif month in zima:
    print("Zima")
elif month in proljece:
    print("Proljece")
elif month in ljeto:
    print("Ljeto")
else:
    print("Greska: uneseni mjesec nije prepoznat!")







'''
Napravite listu s nekoliko naziva slatkiša. Nazovite je slatkisi i ispišite zadanu listu..
    a.Zatražite od korisnika da unese naziv svog omiljenog slatkiša i pohranite u posebnu varijablu
    b.Ako se njegov slatkiš nalazi u listi, ispisati: "Već imamo u asortimanu!"
    c.Ako se ne nalazi u listi, dodati u listu i ispisati modificiranu listu
'''
#12
slatkisi = ["cokolada", "bomboni", "keks", "lizalica", "karamela"]
omiljeni_slatkis = input("Unesi naziv svog omiljenog slatkisa: ").lower()

if omiljeni_slatkis in slatkisi:
    print("Vec imamo u asortimanu!")
else:
    slatkisi.append(omiljeni_slatkis)
    print("Dodali smo tvoj omiljeni slatkis u asortiman.")
    print("Azurirani asortiman:", slatkisi)






'''
Napravite listu s nekoliko naziva povrća koje imate na meniju. Nazovite listu povrce i ispišite njen sadržaj.
    a.Zatražite od korisnika da unese naziv povrća kojeg ne voli i pohranite ga u zasebnu varijablu.
    b.Ako se unešeno povrće ne nalazi na listi, ispisati poruku: "All good!"
    c.Ako se povrće nalazi na listi, pozvati zasebnu vlastitu funkciju koja če obrisati to povrće s liste i ponovo je ispisati.
'''
#13
def ukloni_povrce(povrce, lista_povrca):
    lista_povrca.remove(povrce)
    print(f'Azurirana lista povrca bez {povrce}: {lista_povrca}')

povrce = ["mrkva", "brokula", "kelj", "rajcica", "krastavac"]
print(f'Povrce na meniju: {povrce}')

nevoljeno_povrce = input("Unesi naziv povrca koje ne volis: ").lower()
if nevoljeno_povrce in povrce:
    ukloni_povrce(povrce, nevoljeno_povrce)
else:
    print("All good!")






'''
Zatražite od korisnika da unese neki broj!
    a.Ako je broj pozitivan, ispisuje se poruka: "All good!"
    b.Ako je broj negativan, pozovite funkciju koja će taj broj pretvoriti u pozitivan te ispisati tu novu pozitivnu vrijednost
    c.Ako je broj nula, ispisuje se tekst: "Broj je nula!"
    d.Za sve ostale opcije ispisuje se poruka o grešci!
'''
#14
def negative_to_positive(numero):
    print("Pozitivna vrijednost:", abs(numero))

numero = int(input("Unesi neki broj: "))
if numero > 0:
    print("All good!")
elif numero < 0:
    negative_to_positive(numero)
elif numero == 0:
    print("Broj je nula!")
else:
    print("Nastala je greška!")









'''
Napredniji kalkulator
Unos prvog broja:
 Zatražite od korisnika da unese osnovni broj s kojim će se raditi. Obavezno ga pretvorite u odgovarajući numerički tip (npr. float).
 Zatražite od korisnika da odabere operaciju: želi li &quot;potencirati&quot; ili &quot;korjenovati&quot; broj.
(Npr. neka korisnik unese &quot;p&quot; za potenciranje ili &quot;k&quot; za korjenovanje).
Ovisno o odabiru
 Ako korisnik odabere &quot;potencirati&quot;:
    o Zatražite od korisnika da unese eksponent (na koliko želi potencirati broj
    o Ispišite rezultat potenciranja.
 Ako korisnik odabere &quot;korjenovati&quot;:
    o Zatražite od korisnika da unese stupanj korijena (koji korijen želi izvući).
    o Ispišite rezultat korjenovanja
    o Hint: matematički, korjenovanje se može napisati na sljedeći način:
 Treći korjen iz 27 se može napisati i kao: 27 1/3 (27 potencirano na jednu
trećinu)

 Operacije potenciranja i korjenovanja izvedite preko zasebnih vlastitih funkcija
'''

















