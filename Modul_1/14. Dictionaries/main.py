

proizvod = {
"naziv": "laptop",
"cijena": 1200,
"tezina": 1.5,
"dostupno": True
}
print (proizvod)


#Zadatak 1
voce = {
    "Jabuka" : 2.49,
    "Kruska" : 1.89,
    "Banane" : 1.44
}
print(voce)


automobil = {
    "KIA" : 1.5,
    "Hyundai" : 1.8,
    "Dacia" : 2.0
}
print(automobil)


#Zadatak 2

automobil["Adresa"] = "Ilica"
automobil["Drzava"] = "HR"
print(automobil)

#Zadatak 3
del automobil["KIA"]
print(automobil)
print()




#Zadatak 4
student = {
    "ime" : "Pero", 
    "prosjek" : 4.5,
    "broj_ispita" : 12
}

if student.get("prosjek") >= 4.5 and student.get("broj_ispita") >= 10:
    print(f'Stipendija odobrena za studenta {student.get("ime")}.')
else:
    print(f'Stipendija nije odobrena za studenta {student.get("ime")}.')

print()


#Zadatak 5
kupacA = {
"ime": "Ana",
"ima_karticu_vjernosti": True,
"ukupna_potrosnja": 50.0,
"broj_kupovina": 2
}

kupacB = {
"ime": "Marko",
"ima_karticu_vjernosti": False,
"ukupna_potrosnja": 150.0,
"broj_kupovina": 7
}

print("Kupac A")
if kupacA.get("ima_karticu_vjernosti") == True or (kupacA.get("ukupna_potrosnja") > 100 and kupacA.get("broj_kupovina") > 5 ):
    print("Ostvaruje se superpopust")
else:
    print("Ne ostvaruje se superpopust ")
    
print("------------------------------------------------------------")

print("Kupac B")
if kupacB.get("ima_karticu_vjernosti") == True or (kupacB.get("ukupna_potrosnja") > 100 and kupacB.get("broj_kupovina") > 5 ):
    print("Ostvaruje se superpopust")
else:
    print("Ne ostvaruje se superpopust ")



# Zadatak za grupe: Virtualni aparat za pića

kava = {"ime": "Kava", "cijena": 1.50, "dostupno": True}
caj = {"ime": "Caj", "cijena": 1.20, "dostupno": False}
sok = {"ime": "Sok", "cijena": 2.00, "dostupno": True}
voda = {"ime": "Voda", "cijena": 1.00, "dostupno": True}

def menu():
    print("Nas menu:")
    print(f'1. {kava.get("ime")} - {kava.get("cijena")} EUR')
    print(f'2. {caj.get("ime")} -  {caj.get("cijena")} EUR')
    print(f'3. {sok.get("ime")} - {sok.get("cijena")} EUR')
    print(f'4. {voda.get("ime")} - {voda.get("cijena")} EUR')
    print(f'5. Izlaz')
    print("--------------------------------------")
    return int(input("Unesite broj za zeljeno pice (1. (Kava), 2. (Caj), 3. (Sok), 4. (Voda)) ili ' 5. (Izlaz)' za prekid: "))

def unavailable(beverage):
    print(f'Izabrali ste {beverage}. Trenutno nije dostupan. Molimo odaberite drugo pice.')

def available(beverage, price):
    print(f'Odabrali ste {beverage}. Cijena: {price} EUR')

print("Dobro dosli u Virtualni Aparat za Pica!")
while True:
    choice = menu()
    if choice == 1:
        if kava.get("dostupno"): available(kava.get("ime"), kava.get("cijena"))
        else: unavailable(kava.get("ime"))
    elif choice == 2:
        if caj.get("dostupno"): available(caj.get("ime"), caj.get("cijena"))
        else: unavailable(caj.get("ime"))
    elif choice == 3:
        if sok.get("dostupno"): available(sok.get("ime"), sok.get("cijena"))
        else: unavailable(sok.get("ime"))
    elif choice == 4:
        if voda.get("dostupno"): available(voda.get("ime"), voda.get("cijena"))
        else: unavailable(voda.get("ime"))
    elif choice == 5:
        print("Kraj programa!!!")
        break	

































































