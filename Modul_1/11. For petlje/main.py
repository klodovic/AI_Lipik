
voce = ["jabuka", "banana", "visnja", "jabuka", "kruska", "naranca"]
for vocka in voce:
    print (vocka)
print()


#primjer 1
carobnjaci = ["merlin", "gandalf", "dumbledore"]
for carobnjak in carobnjaci:
    print (f'{carobnjak.title()}, to je bio super trik!')
print()


#Zadatak 1
automobili = ["Audi", "KIA", "Hyundai", "Skoda", "BMW"]
for automobil in automobili:
    print(automobil)
print()


#Zadatak 2
rijeci = ["dobro", "jutro", "svima"]
for rijec in rijeci:
    print(f'{rijec}!')
print()


#Zadatak 3
rijec = "Lipik"
for x in rijec:
    print(x)
print


#Primjer 3
for i in [0, 1, 2, 3]:
    print ("Wuf, wuf, mijau, mijau!")
print()

for i in range(0,100):
    print (f'{i + 1}:  Wuf, wuf, mijau, mijau!')
print()


#Zadatak 4
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i % 2:
        print(f'{i} nije paran broj!')
    else:
        print(f'{i} je paran broj!')
print()


#Zadatak 5
ocjene = [1, 5, 4, 3, 2, 4, 1, 1, 2, 1]
brojac = 0
for i in ocjene:
    if i < 2:
        brojac += 1
print(f'U listi se nalazi {brojac} negativnih ocjena...')
print()


#Zadatk 6
text = "My goal is to make you a better runner. It's as simple as that."
vowels = "aeiou"
counter = 0
for letter in text:
    if letter.lower() in vowels:
        counter += 1
print(counter)
print()

#Zadatak 7
brojevi = [1, 3, 5, 2, 7, 9, 4, 6]        
for broj in brojevi:
    if broj % 2 == 0:
        print(f"Prvi parni broj je: {broj}")
        break
else: #izvršava se samo ako se petlja nije prekinula naredbom break
    print("U listi nema parnih brojeva.")
print()

#Zadatak 8
auti = ["audi", "MERCEDES", "pEUGEOT", "BMW", "fiat"]
for automobil in auti:
    if automobil != automobil.upper():
        print(automobil.title())
    else:
        print(automobil)
print()


#Zadatak 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')



















































