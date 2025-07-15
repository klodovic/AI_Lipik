import math

age = 30
number_of_apples = 12
print(age)
print(number_of_apples)


pi = 3.14159
height = 1.75
print(pi)
print(height)


print(age * 2)
print(number_of_apples / 3)
print(pi + 5)
print(height - 100)

print(pi ** 3)
broj_minuta = 717
print(broj_minuta // 60)

ostatak = broj_minuta % 60
print(ostatak)


##  Zadatak 1

brzina_automobila = 75
broj_sati = 12
udaljenost = broj_minuta * broj_sati
print(f'{udaljenost} km')


## Zadatak 2

promjer = 50
pi = 3.141516
#povrsina = ((promjer/2) * (promjer/2)) * pi
povrsina = pow(promjer/2, 2) * pi
print(f'Površina kruga: {povrsina} mm')


#Operatori usporedbe (>, >=, <, <=, ==, !=)

sati_dan = 8
sati_noc = 8
dnevna_cijena_sata = 40
nocna_cijena_sata = 60

zarada_dan = sati_dan * dnevna_cijena_sata
zarada_noc = sati_noc * nocna_cijena_sata

print(f'Zarada dan je veca od zarada noc: {zarada_dan > zarada_noc}')



### Komentari

# podatci o zaposlenicima
emp_name ="Petar" # employee name
id = 100 # employee id

"""
U ovome modulu smo definirali osnovne podatke o našim zaposlenicima, za potrebe odjela računovodstva
"""

print (emp_name, id)


### Zadatak

cijena = 100
kolicina = 50
pdv = 0.25

#potrebno je izračunati cvijenu s PDV-om te ukupnu cijenu kada se pomnoži s količinom

cijena_s_pdv = (cijena * pdv) + cijena
ukupna_cijena = cijena_s_pdv * kolicina
print(ukupna_cijena)






