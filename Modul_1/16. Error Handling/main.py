import traceback
import os


#zadatak 1

def cijene_s_marzom(cijene, marza):
    nove_cijene= []
    for cijena in cijene:
        nove_cijene.append(cijena - (cijena * marza))
    return nove_cijene

try:
    nabavne_cijene= [25.99, 115.89, 80.59, 55.49]
    postotak_marze = int(input("Molim Vas unesite postotak marže (0 - 100): "))
    print(cijene_s_marzom(nabavne_cijene, postotak_marze / 100))
except Exception as ex:
    print(f'To nije broj. Pokusajte ponovno. {str(ex)}')



#zadatak 2

def index_BMI(visina, tezina):
    return tezina / pow(visina, 2)

def menu():
    print("Glavni menu")
    print("\t1. Izracun \n\t2. Izlaz iz programa ")
    return int(input("Unesite broj: "))

def clear_terminal():
    input(f'Pritisnite Enter za nastavak...')
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    try:
        izbor = menu()
        if izbor < 1 or izbor > 2:
            print(f'Unesite 1 ili 2!!!')
            clear_terminal()
            continue
    
        if izbor == 1:
            visina = float(input("Unesite svoju visinu u metrima: "))
            tezina = int(input("Unesite svoju tezinu u kg: "))
            rezultat = index_BMI(visina=visina, tezina=tezina)
        
        elif izbor == 2:
            print("Hvala sto se ste koristili nas program.")
            clear_terminal()
            break

    except ZeroDivisionError:
        print(f'Nije dozvoljeno dijeliti s 0:')
        clear_terminal()
    except ValueError:
        print(f'To nije broj. Pokusajte ponovno.')
        clear_terminal()
    except Exception as ex:
        print(f'Error: {str(ex)}')
        clear_terminal()
    else:
        print(f'BMI: {rezultat:.2f}')
        clear_terminal()
    finally:
        print("Kraj izracuna!!")



























