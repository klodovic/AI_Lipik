
#usporedba integera
broj1 = 37
broj2 = 10
if broj1 > broj2:
    print ("Prvi boj je veci!")
else:
    print ("Drugi broj je veci!")
print()


#usporedba stringova
auto = "bmw"
if auto == "bmw":
    print ("Volite prave njemacke aute")
else:
    print ("Niste ljubitelj njemackih auta!")
print()



#Operator "in"
omiljeni_auti = ["bmw", "audi", "mercedes"]
auto = "bmw"
if auto in omiljeni_auti:
    print ("Volite prave njemacke aute")
else:
    print ("Niste ljubitelj njemackih auta!")
print()



# Zadatak 1
num1 = 65
num2 = 22

if num1 >= num2:
    print("Moj broj je veci!")
else:
    print("Tvoj broj je veci!")
print()



# Zadatak 2
wifi = "Lipik_online123"
user_pass = "122"

if wifi == user_pass: print("vasa sifra je ispravna")
else: print("vasa sifra nije ispravna")


# Zadatak 3
dostupni_proizvodi = ["banane", "jabuke", "kruske"]
zeljeni_proizvod = "kiwi"

if zeljeni_proizvod in dostupni_proizvodi: print("Proizvod je dostupan")
else: print("Zao nam je, trenutacno proizvod nije u ponudi!")
print()


# Zadatak 4
banned_users = ["pero", "ana", "tea", "marko"]
user = "Jure"

if user.lower() not in banned_users: print("Dobro dosli na nas forum!")
else: print("Zabranjen vam je pristup nasem forumu!")
print()

# Zadatak 5 (and or)

age = 14

if (age >= 8) and (age <= 12): print("Dobro dosli, mozete se igrati!")
else: print("Nazalost ne ispunjavate uvjete, ne mozete pristupiti!")
print()


# Zadatak 6

broj_bodova = 90

if broj_bodova >= 90: print("Ocjena A")
elif (broj_bodova >= 75) and (broj_bodova <= 90): print("Ocjena B")
else: print("Ocjena C")
print()

# Zadatak 7
def movie_menu():
    print("Odaberite jedan zarn filma koji zelite gledati. Od zarnova trenutno imamo u ponudi:")
    print("1. Akcija")
    print("2. Komedija")
    print("3. Drama")
    print("4. Izlaz iz programa")
    return int(input("Unesite jedan od tri ponudena broja: "))

def poruka():
    print("Nepostojeci izbor, pokusajte ponovo....")
    movie_menu()        

def izbor_zarna(zanrovi):
        print(f'Zelite li gledati {zarnovi[0]} ili {zarnovi[1]}?')
        print(f'1. {zanrovi[0]}')
        print(f'2. {zanrovi[1]}')
        return int(input("Unesite jedan od dva ponudena broja: "))


zarn = movie_menu()

if zarn < 1 and zarn > 4:
    print("Odaberite brojeve od 1 do 4...")
    movie_menu()
else:
    if zarn == 1:
        zarnovi = ["Novi", "Klasican"]
        izbor = izbor_zarna(zarnovi)
        if izbor == 1:
            print("Nasa preporuka: Mad Max: Fury Road")
        elif izbor == 2:
            print("Nasa preporuka: Die Hard")
        else:
            poruka()
    elif zarn == 2:
        zarnovi = ["Crna komedija", "Romanticna komedija"]
        izbor = izbor_zarna(zarnovi)
        if izbor == 1:
            print("Nasa preporuka: Death at a Funeral")
        elif izbor == 2:
            print("Nasa preporuka: Crazy Rich Asians")
        else:
            poruka()
    elif zarn == 3:
        zarnovi = ["Povijesna drama", "Suvremena drama"]
        izbor = izbor_zarna(zarnovi)
        if izbor == 1:
            print("Nasa preporuka: Schindler's List")
        elif izbor == 2:
            print("Nasa preporuka: Parasite")
        else:
            poruka()
    elif zarn == 4: exit
    #else: print("Neispravan unos! Odaberite jedan od zarnova: Akcija, Komedija i Drama")























