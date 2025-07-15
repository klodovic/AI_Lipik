'''
1. Napravite listu koja se zove ljubimci. U nju stavite nekoliko naziva životinja te ispišite listu 
'''
pets = ["pas", "macka", "kanarinac", "kunic", "hrcak"]
print(pets)
print()

'''
2. Napravite listu koja se zove temperatura. U nju stavite nekoliko temperatura zraka, od ljeta 
    do zime te ispišite listu 
'''
temp = [-15, -10, -8, 0, 4, 12, 20, 38]
print(temp)
print()

'''
3. Za listu temperatura napravite varijablu u kojoj ćete pohraniti dujinu liste. Duljinu liste ćete 
    izračunati jednom funkcjom iz pythona, ne brojati ručno! 
'''
print(f'Lista temperatura ima {len(temp)} elemenata.')
print()

'''
4. Napravite listu pod nazivom studenti. U njoj se nalaze imena studenata te za svakog od njih njihova 
    prosječna ocjena tokom studija. Ispišite listu 
'''
studenti = [("Ana", 4.5), ("Marko", 3.7), ("Ivana", 4.0), ("Petar", 2.9)]
for ime, prosjek in studenti:
    print(f'{ime} ima prosjek ocjena: {prosjek}')
print()
    
'''
5. Korištenjem naredbe print ispišite iz liste ljubimci one elemente koji se nalaze na samom početku liste te na samom kraju liste. 
'''
print(f'Prvi element liste: {pets[0]}, zadnji element liste: {pets[-1]}')
print()

'''
6. Korištenjem naredbe print, iz liste temperatura ispišite elemente liste koji se nalaze od samog početka do elementa s indeksom 3. 
'''
print(temp[0:3])
print()

'''
7. Kreirajte praznu listu po nazivom izlet. Napunite je s 5 destinacija za izlet. 
    a) Modificirajte listu izlet na način da na sam početak liste ubacite element pod 
    nazivom „Balaton“. 
    b) Ispišite listu 
'''
izlet = []
izlet.append("Italija")
izlet.append("Slovenija")
izlet.append("Grcka")
izlet.append("Austrija")
izlet.append("Island")
izlet.insert(0, "Balaton")
print(izlet)
print()

'''
8. Iz liste ljubimci obrišite dva člana liste. Nanovo ispišite listu. 
'''
print(pets)
pets.pop(2)
pets.pop(3)
print(pets)
print()

'''
9. Napravite listu koja se zove nakit od nekoliko članova. Jedan od elemenata neka bude „zlatna narukvica“. 
    a) Promijenite „zlatnu narukvicu“ u „srebrnu narukvicu“ 
'''
nakit = ["Zlatni sat", "Prsten", "Ogrlica", "Dijamanti", "Kruna", "Zlatna narukvica"]
nakit[nakit.index("Zlatna narukvica")] = "Srebrna narukvica" 
print(nakit)
print()

'''
10. Obrišite sadržaj liste studenti, lista i dalje postoji nakon brisanja, samo je prazna 
'''
studenti.clear()
print(studenti)
print()

'''
11. Napravite listu cijene, u nju stavite tri cijene 
    a) Napravite novu varijablu zbroj u kojoj ćete zbrojiti te tri cijene te je ispišite 
    b) Napravite novu varijablu prosjek u kojoj ćete izračunati prosjek te tri cijene te je 
    ispišite. 
'''
cijene = [12.99, 22.19, 55.09]
total = sum(cijene)
averge = total / len(cijene)
print(f'Ukupna cijena: {total:.2f}, a prosjek iznosi: {averge:.2f}')
print()

'''
12. Organizirate zabavu te ste napravili listu gosti. Definirajte listu gosti u kojoj se nalazi 5 osoba. 
    a) Došlo je do promjene, na zabavi će se pojaviti još jedna osoba. Definirajte vlastitu 
    funkciju uz pomoć koje će dodati još jednu osobu na popis 
    b) Naravno da je opet došlo do promjene, na zabavi će biti jedan vaš jako dobar 
    prijatelj. Ubacite ga na popis gostiju, neka bude na čelu liste! Opet koristite vlastitu 
    funkciju za ubacivanje elementa u listu. 
    c) Jedna osoba je otkazala sudjelovanje. Maknite je iz liste pozivom odgovarajuće 
    vlastite funkcije. 
'''
guests = ["Pero", "Mia", "Tea", "Marko", "Tomo"]

def add_guest(guests_list, guest):
    guests_list.append(guest)
    
def add_guest_on_start(guests_list, guest):
    guests_list.insert(0, guest)
    
def remove_guest(guests_list, guest):
    guests_list.remove(guest)

# a)
add_guest(guests, "Ivana")
print(guests)

# b)
add_guest_on_start(guests, "Filip")
print(guests)

# c)
remove_guest(guests, "Tea")
print(guests)
print()


'''
13. Napravite listu tezina u kojoj se nalazi barem 5 tezina sportaša. Korištenjem sort metode 
    poredajte te veličine od najmanje do najveće. 
'''
weight = [72, 88, 170, 155, 125]
weight.sort()
print(weight)
print()

'''
14. Napravite listu cijene_stanova i stavite u nju barem pet vrijednosti. 
    a) Sortirajte vrijednosti od najmanje do najveće te ih ispišite! 
    b) Sortirajte vrijednosti od najveće do najmanje te ih ispišite! 
'''
cijene_stanova = [150.000, 605.500, 311.000, 250.540, 809.250]
print(cijene_stanova)
cijene_stanova.sort()
print(cijene_stanova)
cijene_stanova.sort(reverse=True)
print(cijene_stanova)
print()

'''
15. Napravite sljedeću listu: slova = [1, 2, 3, 4, 5] 
    a) Zamijenite prvi i zadnji element u listi i ispišite rezultat 
    b) Vaš rezultat treba glasiti: slova = [5, 2, 3, 4, 1]
'''
slova = [1, 2, 3, 4, 5]
print(slova)
prvi_element = slova[0]
slova[0] = slova[-1]
slova[-1] = prvi_element
print(slova)



















