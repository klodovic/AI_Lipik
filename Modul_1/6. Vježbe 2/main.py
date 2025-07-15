import math

print("Zadatak 1")
""" 1.	Odredite tip podatka ovih varijabli i ispišite rezultat na ekranu:
        a.	tezina = 87.55
        b.	visina = ''192 cm''
        c.	naziv_hotela = ''Hotel Bellevue''
        d.	telefon = ''01/458-698''
        e.	placeno = True
 """

tezina = 87.55
visina = '192 cm'
naziv_hotela = 'Hotel Bellevue'
telefon = '01/458-698'
placeno = True
print(f'Tezina: {type(tezina)}')
print(f'Visina: {type(visina)}')
print(f'Naziv hotela: {type(naziv_hotela)}')
print(f'Telefon: {type(telefon)}')
print(f'Placeno: {type(placeno)}')
print()


print("Zadatak 2")
""" 2.	Od korisnika se traži da unese svoje ime, a nakon toga svoje prezime. Svaki od odgovora pohranite u posebnu varijablu
    a.	Na primjer, korisnik je prvo unio ime Pero, a nakon toga prezime Perić
    b.	Ispišite pozdravnu poruku u kojoj će se zamijeniti redoslijed imena i prezimena
    c.	Na primjer: ''Pozdrav Perić Pero''
 """

first_name = input("Unesite svoje ime: ")
last_name = input("Unesite svoje prezime: ")
print(f'Pozdrav {last_name} {first_name}')
print()


print("Zadatak 3")
""" 3.	Od korisnika se na ekranu traži da unese svoj najdraži broj
    a.	Korištenjem odgovarajućih funkcija, pretvorite unos u cijeli broj, odnosno decimalni broj
 """
 
fav_num = input("Unesite svoj najdraži broj: ")
int_num = int(fav_num)
print(fav_num)
float_num = float(fav_num)
print(float_num)
print()


print("Zadatak 4")
""" 4.	Napišite program koji će od korisnika zatražiti da unese polumjer kruga.
    a.	 Program će zatim izračunati i ispisati površinu kruga. 
    b.	Koristiti konstantu pi = 3.14159
    c.	Komentirajte vaš kod!
 """
r = float(input("Unesite polumjer kruga: "))
PI = 3.14159
print(f'Povrsina kruga iznosi: {pow(r, 2) * PI}')
print()


print("Zadatak 5")
""" 5.	Napišite program koji će od korisnika zatražiti da unese neki broj
    a.	Unešeni broj pomnožite s broj 5
    b.	Ispišite rezultat
 """
num = int(input("Unesite neki broj: "))
print(num * 5)
print()


print("Zadatak 6")
""" 6.	Od korisnika se traži da unese neki cijeli broj(n)
    a.	Izračunajte n + nn + nnn
    b.	Na primjer, korisnik je unio broj 7, potrebno je izračunati 7 + 77 + 777
    c.	Stavite komentare u vaš kod
    d.	Ispišite rezultat
 """

n = int(input("Unesite neki broj: "))
print(n + (n*10 + n) + ((n * 100) + (n * 10) + n)) #model za izracun (7 + 77 + 777)
print()


print("Zadatak 7")
""" 7.	Napišite program koji od korisnika traži da unese udaljenost između neka dva mjesta u miljama
    a.	Izračunajte koliko ta udaljenost iznosi u kilometrima
    b.	Ispišite rezul
 """
distance = float(input("Unesite udaljenost izmedu dva mjesta izrazeno u miljama: "))
MILE = 1.609344
print(distance * MILE)
print()


print("Zadatak 8")

""" 8.	Napišite program u kojem se traži od korisnika da unese neki broj
    a.	Izračunajte razliku između tog broja i broja 20
    b.	Ispišite rezultat
 """
number = int(input("Unesite neki broj: ")) #
diff = abs(20 - number)
print(diff)
print()


print("Zadatak 9")
""" 9.	Napišite program u Pythonu koji od korisnika traži da unese koliko sati traje put između dva mjesta
    a.	Ispišite koliko traje put u minutama
    b.	Na primjer, korisnik je unio trajanje puta od 3.5 sati. Treba se ispisati broj 210
 """

time_in_hours = float(input("Koliko sati traje put između dva mjesta: ")) 
time_in_minutes = time_in_hours * 60
print(int(time_in_minutes))
print()


print("Zadatak 10")
""" 10.	Zatražite od korisnika da unese svoje ime i prezime. Podatke pohranite u zasebnu varijablu
    a.	Promijenite sva slova u velika
    b.	Ispišite na ekranu duljinu unešenog imena i prezimena
    c.	Komentirajte vaš kod!
 """

first_name = input("Unesite svoje ime: ").upper()
last_name = input("Unesite svoje prezime:").upper()
print(f'Duljina imena iznosi {len(first_name)} znaka, a duljina prezimena iznosi {len(last_name)} znaka.')
print()


print("Zadatak 11")
""" 11.	Zatražite od korisnika da unese broj koji predstavlja broj dana dostave i pohranite tu vrijednost u varijablu dani_do_dostave
    a.	Generirajte korisničku poruku koja glasi:
    "Vaša narudžba će biti dostavljena za dani_do_dostave  dana."
 """

dani_do_dostave = input("Unesite broj dana do dostave: ")
print("Vaša narudžba će biti dostavljena za " + dani_do_dostave + " dana!")
print()


print("Zadatak 12")
""" 12.	Definirajte tri tekstualne varijable. 
    a.	Korištenjem ulančavanja spojite ih u jednu
    b.	Korištenjem funkcije len() odredite duljinu tog novog stringa.
    c.	Ispišite rezultat.
 """
str_1 = "Ivana"
str_2 = "Brlic"
str_3 = "Mazuranic"
text = str_1 + " " + str_2 + " " + str_3
print("Duljina novog stringa je: " + str(len(text)))
print()


print("Zadatak 13")
""" 13.	Zatražite od korisnika da unese neki broj!
    a.	Provjerite je li taj broj jednak broju 75
    b.	Ispišite rezultat!
 """
number = int(input("Unesite neki broj: "))
print("Je li uneseni broj jedan broju 75? " + str(number == 75))
print()


print("Zadatak 14")
""" 14.	Zatražite od korisnika da unese dva broja
    a.	Usporedite je li prvi broj veći od drugog
    b.	Ispišite rezultat!
 """
num_1 = int(input("Unesite prvi broj: "))
num_2 = int(input("Unesite drugi broj: "))
print("Je li prvi broj veći od drugog? " + str(num_1 > num_2))
print()


print("Zadatak 15")
""" 15.	Zatražite od korisnika da unese neki broj!
    a.	Provjerite je li zaj broj različit od broja 2024
    b.	Ispišite rezultat!
 """
some_num = int(input("Unesite neki broj: "))
print("Je li uneseni broj različit od broja 2024? " + str(some_num != 2024))
print()







