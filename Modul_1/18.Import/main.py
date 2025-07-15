import modul_sum 
import multi as m
import statistics as stat
import sys
import pandas as pd
import matplotlib.pyplot as plt
# glavni_program.py

""" print("--- Primjer korištenja vlastitog modula ---")
broj1 = float(input("Unesi prvi broj: "))
broj2 = float(input("Unesi drugi broj: "))
# Koristimo sintaksu: ImeModula.ImeFunkcije(argumenti)
rezultat = modul_sum.sum(broj1, broj2)


print ("Zbroj glasi: ", rezultat)
print("Program je završio s radom.")

 """

print(m.mul(10, 12))

#zadatak 2
place = [1000, 1200, 850, 750, 1300, 1400, 42000, 1500, 1050, 920]
print(stat.mean(place))
print(stat.median(place))


placanje =["kartica", "gotovina", "kartica", "kartica", "paypal", "kartica"]
print(stat.mode(placanje))


#Zadatak 3
def list_clean(list_to_clean):
    temp = []
    for item in list_to_clean:
        if item != 999.0:
            temp.append(item)
    return temp

try:
    sirova_ocitanja = [20.5, 21.0, 999.0, 19.8, 22.3, 999.0, 20.1, 25.0, 999.0, 21.5]
    prosjek = stat.mean(list_clean(sirova_ocitanja))
except stat.StatisticsError as ex:
    print(f'Dogodila se greska! Objasnjenje: {str(ex).title()}')
else:
    print(f'Prosjecna vrijednost temperature iznosi: {prosjek:.2f} C')



#Primjer 3 - Pandas i Matplotlib
data = pd.read_csv("C:\\Users\\Next Design\\Desktop\Modul1\\18.Import\\Advertising.csv")

print(data.head(15))
print (data.describe())

""" plt.scatter(data['TV'], data['sales'], color='blue', alpha=0.6)
plt.title("TV oglašavanje vs. Prodaja")
plt.xlabel("Potrošnja na TV oglase (u 1000 USD)")
plt.ylabel("Prodaja proizvoda (u 1000 jedinica)")
plt.grid(True)
plt.show()
 """

plt.figure(figsize=(20, 10))
plt.plot(data['TV'], label='TV', color='red')
plt.plot(data['radio'], label='Radio', color='green')
plt.plot(data['newspaper'], label='Novine', color='orange')
plt.title("Usporedba ulaganja u reklamu")
plt.xlabel("Redni broj unosa")
plt.ylabel("Iznos ulaganja (u 1000 USD)")
plt.legend()
plt.show()
# --- KOD ZA GRAFIČKI PRIKAZ ---

# Kreiranje scatter (raspršenog) grafa
# Na x-osi prikazujemo 'TV' potrošnju
# Na y-osi prikazujemo 'sales' (prodaju)
plt.figure(figsize=(10, 6)) # Postavljanje veličine grafa (širina, visina)
plt.scatter(data['TV'], data['sales'], alpha=0.7) # alpha=0.7 čini točke malo prozirnima

# Dodavanje naslova grafu i oznaka osima
plt.title('Usporedba TV budžeta i prodaje', fontsize=16)
plt.xlabel('TV budžet (u tisućama $)', fontsize=12)
plt.ylabel('Prodaja (u jedinicama)', fontsize=12)

# Dodavanje mreže za bolju čitljivost
plt.grid(True, linestyle='--', alpha=0.6)

# Prikaz grafa
plt.show()

print("Program je završio s radom.")









































































