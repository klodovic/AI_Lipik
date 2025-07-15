

gradovi = ["Zagreb", "Split", "Osijek", "Pula", "Rijeka"]
cijene = [5, 9, 12, 15.5, -7.3]
odgovori = [5, 3, "dobro", 1, "dobro", "odlicno"]

sportasi = ["Baturina", "Modric", "Budimir", "Kacavenda", "Stojkovic"]
automobili = ["Audi", "KIA", "Hyundai", "Skoda", "BMW"]
ocjene = [5, 4, 4, 3, 4]

print(gradovi)
print(gradovi[2])
print(gradovi[-3])
print(gradovi[1:3])

inventory = ["noz", "mac", "pistolj", "stit", "bomba", "pancirka"]
print(inventory)
print(inventory[0:4])
print(inventory[len(inventory) - 4: len(inventory)])

gradovi.append("Karlovac")
gradovi.append("Sisak")
print(gradovi)


popis_kupovina = []
popis_kupovina.append ("kruh")
popis_kupovina.append ("novine")
popis_kupovina.append ("kava")
print (popis_kupovina)


#vjezba 2
slatkisi = ["cokolada", "bomboni", "keksi", "sladoled"]
print(slatkisi)

#vjezba 3
# destinacije = []
# destinacije.append(input("Unesite mjesto koje biste htjeli posjetiti: "))
# destinacije.append(input("Unesite drugo mjesto koje biste htjeli posjetiti: "))
# print(f'Tokom vašeg odmora posjetit ćete ova mjesta: {destinacije[0]} i {destinacije[1]}')


gradovi.insert(1, "Zadar")
print(gradovi)


alieni = ["patuljak", "vilenjak", "predator"]
alieni.remove("vilenjak")
print (alieni)


slatkisi.remove("keksi")
print(slatkisi)



gradovi.pop(2)
print(gradovi)
print("\n")


#vjezbe 4
shopping_cart = ["hlace", "kaput", "remen"]
shopping_cart.append("zimska kapa")
shopping_cart.append("rukavice")
shopping_cart.remove("remen")
shopping_cart[1] = "zimska jakna"
print(shopping_cart)


gradovi_sjever =["Zagreb", "Karlovac", "Sisak"]
gradovi_jug = ["Split",
"Zadar", "Rijeka"]
hrvatska = gradovi_sjever + gradovi_jug
print (hrvatska)

biljke = ["hrast", "jagoda", "banana", "kaktus"]
print(biljke)
biljke.clear()
print(biljke)


#zadatak 5
prvi_razred = ["Pero", "Ivan", "Tea"]
prvi_razred.clear()
print(prvi_razred)


cijene = [5, 10, 27, 43, 11, 4, 39, 51]
del cijene[2:5]
print (cijene)

#zadatak 6
vrucina = [30, 17]
razlika_temp = vrucina[0] - vrucina[1]
print(razlika_temp)



kosarica = ["sol", "papar", "kim", "anis", "vlasac"]
print (kosarica)
kosarica.sort()
print(kosarica)
kosarica.reverse()
print (kosarica)



visina_sportasa = [157, 192, 148, 179, 201]
print (visina_sportasa)
visina_sportasa.sort(reverse = True)
print (visina_sportasa)



print(gradovi)

def remove_town(towns, index):
    towns.pop(index)
    return towns
    
gradovi = remove_town(gradovi, index=2)
print(gradovi)




























