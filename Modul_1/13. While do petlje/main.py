import random


#Primjer 1
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#Primjer 2
def zbrajanje (a,b):
    return a + b

print ("Dobro došli jednostavnu kalkulator aplikaciju")

while True:
    print ("Za zbrajanje dva broja, unesite riječ 'zbrajanje")
    print ("Upišite 'quit' ako želite završiti")
    odgovor = input ("Vaš odgovor: ")
   
    if odgovor == "quit":
        print ("Zahvaljujem na korištenju")
        break
    if odgovor == "zbrajanje":
        broj1 = float(input("Unesite prvi broj"))
        broj2 = float(input("Unesite drugi broj"))
        rezultat = zbrajanje (broj1, broj2)
        print ("Zbroj vaša dva broja glasi:", rezultat)
       
print ("kaj programa")





#Zadatak 1
while True:
    grad  = input("Unesite naziv grada: ")
    print(f'{grad.title()} je prekrasan u ovo doba godine!')
    izbor  = input("Zelite li nastaviti? (Da/Ne): ")
    if izbor == "Ne":
        break

 
 ### Random 
 
 #Primjer 1
slucajni_broj = random.randint(1, 100)
print (slucajni_broj)


#Zadatak Random
random_num = random.randint(1, 10)
while True:
    #print(random_num)
    user_num = int(input("Unesite neki broj od 1 do 10: "))
    if user_num < random_num:
        print("Vas broj je manji.")
    elif user_num > random_num:
        print("Vas broj je veci.")
    else:
        print("Pogodili ste broj!!!")
        break


""" Napišite program koji simulira jednostavnu aplikaciju za vođenje popisa obaveza ("ToDo" lista). 
    Program treba korisniku omogućiti dodavanje, prikazivanje i brisanje zadataka s popisa. 
    Upute: 
        1. Na početku programa, stvorite praznu listu koja će služiti za pohranu vaših zadataka. 
        Nazovite je zadaci. 
        2. Program treba neprekidno nuditi korisniku sljedeće opcije putem brojeva:  
            1. Dodaj zadatak: Korisnik unosi tekstualni opis novog zadatka, koji se zatim dodaje 
            na kraj liste zadaci. 
        2. Prikaži zadatke: Program ispisuje sve trenutne zadatke iz liste. Ako nema zadataka, ispišite poruku da je lista prazna. 
            0. Izlaz: Program završava rad. 
        3. Koristite while petlju kako bi se izbornik neprekidno prikazivao dok korisnik ne odabere izlaz. 
            Bonus zadatak: unesite i dodatnu opciju za brisanje zadataka s To Do liste
 """

tasks = []

def menu():
    print("Odaberite zadatak:")
    print("1. Dodaj zadatak")
    print("2. Prikazi zadatke")
    print("3. Obrisi zadatak")
    print("4. Izlaz iz programa")
    return int(input("Unesite jedan od tri ponudena broja: "))

def error_user_input():
    print("Pogresan unos korisnika....")
    print("Molim, unesite broj od 1 do 3!!")
    
def list_print():
    i = 1
    for task in tasks:
        print(f'{i}. {task}')
        i = i + 1

while True:
    choice = menu()
    
    if choice < 1 or choice > 4:
        error_user_input()
        
    elif choice == 1:
        tasks.append(input("Unesite zadatak na ToDo listu: "))
        list_print()
        
    elif choice == 2:
        if tasks == []:
            print("############   Nemate zadataka za prikaz....  #############")
        list_print()   
                         
    elif choice == 3:
        if tasks == []:
            print("############   Nemate zadataka za brisanje....  #############")
            continue
            
        list_print()
        task_id = int(input("Unesite zadatak koji zelite obrisati: "))
        tasks.pop(task_id - 1)
        list_print()

    elif choice == 4:
        print("Upozorenje! Izgubit cete sve unesene podatke....")
        response = input("Jeste li sigurni? (Da/Ne): ")
        if response == "Da":
            print("Kraj programa")
            break























































































