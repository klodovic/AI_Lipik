import math


def potenciranje(num, potencija):
    return pow(num, potencija)

def korijenovanje(num, stupanj):
    return pow(num, 1 / stupanj)

num_1 = float(input("Unesi neki broj"))
operacija = input("Unesi operaciju koju zelite izvrsiti: 'p' za potenciranje, 'k' za korjenovanje):  ").lower()

if operacija == "p":
    potencija = int(input("Unesi eksponent "))
    print(potenciranje(num_1, potencija))
elif operacija == "k":
    stupanj = int(input("Unesi stupanj korjena "))
    print(korijenovanje(num_1, stupanj))
else: 
    print("Pogresan unos....")
    
    