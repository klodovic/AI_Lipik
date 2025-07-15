# poruka = "Dobro došli u Lipik..."
# print(poruka)

# poruka  = "Dobro došli na tečaj programiranja u Lipiku..."
# print(poruka)


# ime = "Josip"
# mjesto_rodjenja = "Zagreb"
# godina_rodjenja = 1977
# visina = 180

# print(f'Ime: {ime} \nMjesto rodjenja: {mjesto_rodjenja} \nGodina rodjenja: {godina_rodjenja} \nVisina: {visina}')

glazbenica = "celine dione"
glazbenica = glazbenica.title()
print(glazbenica)


grad = "zagreb"
drzava = "SJEDINJENE AMERIČKE DRŽAVE"
ulica = "Iločka ulica 15b"

grad = grad.title()
drzava = drzava.title()
ulica = ulica.title()

print(grad, drzava, ulica)


marka_automobila = "bmw"
povrce = "PAPRIKA"

marka_automobila = marka_automobila.upper()
povrce = povrce.lower().title()

print(povrce + ', ' + marka_automobila)



prvo_mjesto = "    Zadar"
drugo_mjesto = "Osijek    "
trece_mjesto = "   Rijeka    "

prvo_mjesto = prvo_mjesto.lstrip()
drugo_mjesto = drugo_mjesto.rstrip()
trece_mjesto = trece_mjesto.strip()

print(prvo_mjesto, drugo_mjesto, trece_mjesto)


naselje = "grad nova gradiška"
tip_naselja, naziv_naselja = naselje.split(" ", 1)
print(tip_naselja.title(), naziv_naselja.title())


direktorij = "/home/korisnik/dokumenti/"
ime_datoteke = "izvjestaj.txt"

url = direktorij + ime_datoteke
print(url)






