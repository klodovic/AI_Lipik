import math

"""
1.	Deklarirajte varijablu u kojoj ćete pohraniti naziv srednje škole koju ste završili. Deklarirajte varijablu u kojoj ćete navesti koliko 
    imate ukupno braće i sestara. 
        a.	Ispišite rezultate
        b.	Dobili ste još jednu seku, čestitam! Ažurirajte vrijednost varijable te ponovo ispišite vrijednosti
"""
print("Zadatak 1")
school_name = "Elektrostrojarska obrtnicka skola"
siblings = 1

print(f'Naziv zavrsene skole: {school_name}')
print(f'Broj brace i sestara: {siblings}')
siblings += 1
print(f'Broj brace i sestara: {siblings}')
print("\n")

"""
2.	Imate varijablu sjediste u kojoj piše tekst: ''Uprava, Ilica 1, 10 000 Zagreb''. Na odgovarajući način podijelite ovaj string u tri dijela, 
    kao separator se koristi znakovi '', ''. Svaki dio je pohranjen u novoj varijabli
        a.	Ispišite te tri varijable
"""

print("Zadatak 2")
venue = "Uprava, Ilica 1, 10 000 Zagreb"
name, street, post_number = venue.split(", ", 2)
print(f'Naziv: {name}, Ulica: {street}, Postanski broj: {post_number}')
print("\n")


"""
3.	Deklarirajte varijablu ustanova u kojoj se nalazi tekst SVEUČILIŠTE JOSIPA JURJA STROSSMAYERA U OSIJEKU (sve je pisano velikim slovima).  
    Popravite sadržaj ove varijable na način da su sva slova u tom tekstu mala osim početnih slova riječi.
        a.	Ispišite rezultat
"""

print("Zadatak 3")
institution = "SVEUČILIŠTE JOSIPA JURJA STROSSMAYERA U OSIJEKU"
institution = institution.lower().title()
print(institution)
print("\n")


"""
4.	Deklarirajte varijablu ulica = ''Savska cesta'' te varijablu kucni_broj = '' 37A'
    a.	Na odgovarajući način deklarirajte novu varijablu adresa u kojoj će se nalaziti spoj ove dvije varijable (''Savska cesta 37A'').
    b.	Ispišite rezultat
"""

print("Zadatak 4")
street_name = "Savska cesta"
street_number = "37A"
address = street_name + ' ' + street_number
print(address)
print("\n")

"""
5.	Korinisnik je na web portalu prilikom upisivanja imena svog ljubimca slučajno stavio nekoliko razmaka prije imena. 
    Deklarirajte varijablu ime_ljubimca, pohranite u nju neko ime s nekoliko razmaka prije imena te odgovarajućom metodom maknite razmake
        a.	Ispišite ime ljubimca prije popravka i nakon popravka
"""

print("Zadatak 5")
pet_name = "  Garfield"
pet_name = pet_name.lstrip()
print(pet_name)
print("\n")


"""
6.	Korištenjem naredbe print i odgovarajuće operacije, ispišite 25 puta zaredom riječ Super
"""

print("Zadatak 6")
print("Super" * 25)
print("\n")


"""
7.	Pronađite izreku neke poznate osobe. Ispišite autora te izreku na ekranu, nije potrebno pohranjivati u varijablu
    a.	Primjer: Mark Twain je rekao: ''Kada pecate ljubav, neka vam za mamac posluži srce a ne mozak.''
    b.	Navodnici oko izreke su obavezni, pazite kako ćete to izvesti
"""

print("Zadatak 7")
print('"Be yourself! Everyone else is already taken." - Oscar Wilde')
print("\n")



"""
8.	Deklarirajte varijablu cijena_jabuke i u nju pohranite neki broj. Deklarirajte varijablu kolicina i u nju isto pohranite neki broj.
    a.	Deklarirajte novu varijablu ukupno u koju ćete pohraniti koliko koštaju jabuke
    b.	Ispišite rezultat 
"""

print("Zadatak 8")
apple_price = 2.45
quantity = 2
apple_price = apple_price * quantity
print(f'Jabuke kostaju: {apple_price}eur.')
print("\n")


"""
9.	Deklarirajte 5 varijabli u kojima ćete pohraniti brojčane vrijednosti (prvi_broj, drugi_broj, treći_broj itd). 
    a.	Napravite novu varijablu u kojoj ćete izračunati njihovu sumu. 
    b.	Napravite još jednu varijablu te u njoj izračunajte aritmetičku sredinu tih 5 brojeva
    c.	Ispišite te vrijednosti
"""

print("Zadatak 9")
num1 = 5
num2 = 7
num3 = 16
num4 = 54
num5 = 38

num_sum = num1 + num2 + num3 + num4 + num5
averge = num_sum / 5
print(f'Suma brojeva: {num_sum}')
print(f'Srednja vrijednost: {averge}')

print("\n")




"""
10.	Deklarirajte dvije varijable pod nazivom duljina_sobe i sirina_sobe u kojima ćete pohraniti duljinu i širinu vaše sobe.
    a.	Napravite novu varijablu u kojoj ćete izračunati površinu vaše sobe.
    b.	Ispišite rezultat
"""

print("Zadatak 10")
room_length = 2.5
room_width = 4.3
area = room_length * room_width
print(f'Povrsina sobe: {area}m2.')

print("\n")


"""
11.	Danas je 2024. godina. Deklarirajte varijablu u kojoj ćete pohraniti godinu vašeg rođenja. 
    a.	Korištenjem ta dva podatka izračunajte svoju starost i pohranite je u novu varijablu
    b.	Ispišite rezultat!
    
    + 
    
    15.	Za zadatke 11 (izračun vaše starosti) te zadatak 13 (BMI index) napišite komentare u kodu
"""

print("Zadatak 11")
year_of_birth = 1977 #godina rodjenja
current_year = 2024 #trenitna godina
years_old = current_year - year_of_birth #izracun starosti osobe
print(f'Starosna dob: {years_old} godina.') #ispis

print("\n")



"""
12.	Deklarirajte varijablu iznos_kune i u nju pohranite neku vrijednost. Deklarirajte novu varijablu tecaj koja iznosi 7.54.
    a.	Deklarirajte novu varijablu u kojoj pohranjujete iznos kuna preračunat u eure.
    b.	Ispišite rezultat
"""

print("Zadatak 12")
amount_kuna = 120.56
exchange_rate = 7.54
amount_euro = amount_kuna / exchange_rate
print(f'Eura: {round(amount_euro, 2)}')

print("\n")


"""
13.	Napravite varijable u kojima ćete pohraniti svoju težinu i visinu. Težinu pohranite u kilogramima, a visinu u metrima
    a.	Pronađite formulu za računanje BMI (Body Mass Index) te ga izračunajte
    b.	Ispišite rezultat
    
    +
    
    15.	Za zadatke 11 (izračun vaše starosti) te zadatak 13 (BMI index) napišite komentare u kodu
"""

print("Zadatak 13")
weight = 90  #težina
height = 1.80 #visina
bmi = 90/pow(height, 2) # izracun BMI
print(f'BMI: {round(bmi, 2)}') #ispis BMI s dvije decimale

print("\n")


"""
14.	Zaposlenik je radio na nekom projektu. Napravite varijablu broj_radnih_sati i u nju pohranite neki broj veći od 100
    a.	Korištenjem odgovarajuće operacije izračunajte koliko je osoba radila punih radnih dana. Radni dan iznosi 8 sati. Ostatak zanemarite
    b.	Ispišite rezultat
"""

print("Zadatak 14")
working_hours = 255
working_days = working_hours // 8
print(f'Ukupno radnih dana: {working_days}')

print("\n")


"""
14.	Zaposlenik je radio na nekom projektu. Napravite varijablu broj_radnih_sati i u nju pohranite neki broj veći od 100
    a.	Korištenjem odgovarajuće operacije izračunajte koliko je osoba radila punih radnih dana. Radni dan iznosi 8 sati. Ostatak zanemarite
    b.	Ispišite rezultat
"""

print("Zadatak 14")
working_hours = 255
working_days = working_hours // 8
print(f'Ukupno radnih dana: {working_days}')

print("\n")



"""
16.	U SAD - u se duljina suknje mjeri u inchima. Iamte jednu američku sunknju duljine 14 incha te jednu europsku suknju duljine 30 cm. 
    Odredite korištenjem operatora usporedbe je li američka suknja dulja?
    a.	Jedan inch iznosi 2,54 cm
    b.	Komentirajte kod
"""

print("Zadatak 16")
len_inch = 14
len_cm = 30
converted_to_cm = len_inch * 2.54

print(f'Je li americka suknja dulja: {converted_to_cm == len_cm}')

print("\n")


"""
17.	Uspoređujete težinu cupcakeova (jako fini kolač 😊) iz UK-a i iz konetinentalnog dijela Europe. 
    Britanski cupcake teži 4 unce, a cupcake iz Francuske teži 120 grama. Odredite korištenjem operatora usporedbe je li 
    britanski cupcake teži od francuskog?
    a.	Jedna unca iznosi 28,34 grama
    b.	Komentirajte kod
"""

print("Zadatak 17")
weight_unce = 4
weight_grams = 120
converted_to_grams = weight_unce * 28.34

print(f'Je li britanski cupcake tezi od francuskog: {converted_to_grams == weight_grams}')

print("\n")

