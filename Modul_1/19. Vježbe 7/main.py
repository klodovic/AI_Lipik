
import statistics as stat
'''
Imamo rječnik koji predstavlja zalihu artikala u skladištu. Napiši program koji traži unos naziva artikla i ispisuje je li artikl dostupan ili ne.
'''


skladiste = {
    "čekić": 5,
    "odvijač": 0,
    "kliješta": 3,
    "šaraf": 20
}


'''
Zadana je lista proizvoda i njihovih cijena. Ako je cijena veća od 100 €, odobri popust od 20%. Ispiši novu cijenu za svaki proizvod.
'''

proizvodi = {
    "Monitor": 150,
    "Miš": 25,
    "Tipkovnica": 45,
    "Laptop": 800,
    "USB stick": 15
}

""" for proizvod in proizvodi:
    if proizvodi[proizvod] > 100:
        proizvodi[proizvod]=proizvodi[proizvod]*0.8
        
print(proizvodi)
 """

'''
Zadana je lista rezultata testova učenika. Program treba:
Izračunati prosječnu vrijednost  i medijan .
Ispisati sve rezultate iznad prosjeka.
Provjeriti je li medijan veći od srednje vrijednosti, pa ispisati odgovarajuću poruku o raspodjeli 
(npr. "Većina učenika ima niže rezultate" ili "Rezultati su ravnomjerno raspoređeni").
rezultati = [65, 70, 75, 80, 85, 90, 95, 100, 100]

'''


rezultati = [65, 70, 75, 80, 85, 90, 95, 100, 100]


ave = stat.mean(rezultati)
median  = stat.median(rezultati)

print(f'Srednja vrijednost {ave}')
print(f'Median {median}')

for r in rezultati:
    if r > ave:
        print(r)

if median > ave:
    print("Vecina ucenika ima nize rezultate...")


















































































