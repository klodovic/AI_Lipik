import functions as f


""" 1.	Napravite funkciju koju kad pozovete, kao rezultat vam ispisuje lijepu poruku za dobro jutro.
"""
f.greeting()
print()


""" 2.	Napravite funkciju koja ima dva parametra (sport i sportas)
            a.	Pozovite funkciju te korištenjem pozicijskih argumenata proslijedite joj podatke o vašem najdražem sportu i sportašu
            b.	Kao rezultat, funkcija bi trebala ispisati tekst sličan:
            Goran Ivanišević i tenis, što poželjeti više!
"""
f.sport("tenis", "Goran Ivanisevic")
print()


""" 3.	Napravite funkciju pod nazivom „pozivnica“ u kojoj ćete koristiti dva argumenta (ime i mjesto)
        a.	Pri pozivu funkcije proslijedite tražene vrijednosti koristeći pozicijske argumente, a kao rezultat se ispisuje poruka slična:
        Pozdrav Poštovani/a Marko
        Pozivamo vas na svečani domjenak 20 12. u Restoran Matejuška
"""
f.pozivnica("Marko", "Didov san")
print()


""" 4.	Napravite funkciju „filmovi“ u kojoj imate dva argumenta, za film i žanr.
        a.	Pri pozivanju funkcije koristite keyword argumente te se kao rezultat ispisuje poruka slična:
        Danas, filmska večer, komedija Sam u kući
"""
f.filmovi(movie="Home alone", gerne="Comedy")
print()


""" 5.	Napravite funkciju koja računa razliku dva broja
    a.	Pri pozivu funkcije koristite keyword argumente te ispišite rezultat
"""
print(f'Razlika izmedu dva broja iznosi: {f.difference_number(x=-15, y=20)}')
print()


""" 6.	Napravit ćete funkciju koja konvertira iznos u kunama u eure. 
        a.	Od korisnika tražite da unese iznos u kunama koje bi htio pretvoriti u eure. Odgovor pohranite.
        b.	Pozovite funkciju te joj kao argument stavite korisnikov iznos u kunama
        c.	Ispišite rezultat
"""
kune = float(input("Unesite iznos u HRK koji zelite pretvoriti u EUR: "))
print(f'Uneseni iznos {kune:.2f}kn = {round(f.konverzija(kune), 2)}eur.')
print()


""" 7.	Definirajte funkciju koja služi da sva slova u stringu koji je predan kao argument, postanu mala slova
        a.	Rješenje morate nakon poziva funkcije vratiti nazad korištenjem returna
        b.	Provjerite radi li funkcija na stringu „NJEMAČKI JEZIK“
"""
print(f'Return with lower letters: {f.lower_letters("NJEMACKI JEZIK")}')
print()


""" 8.	Napravit ćete funkciju prosjecna_brzina koja računa prosječnu brzinu motocikla
        a.	Od korisnika tražite da unese pređenu udaljenost. Odgovor pohranite.
        b.	Od korisnika zatražite da unese potrebno vrijeme za prijeći tu udajenost, u satima. Odgovor pohranite.
        c.	Pozovite funkciju prosjecna_brzina te joj kao pozicijske argumente stavite odgovore korisnika
        d.	Unutar funkcije izračunajte prosječnu brzinu te rješenje vratite nazad korištenjem returna
        e.	Ispišite rezultat uz neku lijepu poruku
"""
udaljenost = float(input("Unesite predenu udaljenost: "))
vrijeme = float(input("Unesite vrijeme izrazeno u satima: "))
print(f"Prosječna brzina motocikla je {f.prosjecna_brzina(udaljenost, vrijeme):.2f} km/h.")
print()



""" 9.	Definirajte funkciju koja dobiva dva broja kao ulaz te izračuna prvo cjelobrojno dijeljenje ta dva broja, a nakon toga računa ostatak 
    dijeljenja ta dva broja
        a.	Oba rješenja nakon poziva funkcije vratiti nazad korištenjem returna
        b.	Primjer: Pozivamo funkciju kojoj dajemo argumente 15 i 6
        c.	Kao rezultat cjelobrojnog dijeljenja dobit ćemo broj 2, a ostatak dijeljenja bi iznosio 3
"""
cijeli_broj, ostatak = f.number_division(x=15, y=6)
print(f'Rezultat cjelobrojnog dijeljenja = {cijeli_broj}, a ostatak dijeljenja = {ostatak}')
print()


""" 10.	Napravite funkciju koja nam služi za pretvaranje iznosa eura u švicarske franke. 
        a.	Funkcija ima dva parametra, količinu eura i tečaj. Za tečaj koristite defaultnu vrijednost od 0.94
        b.	Pozovite funkciju i zadajte samo vrijednost za količinu
        c.	Vratite rezultat korištenjem returna
"""
euros = 10
print(f'{euros:.2f} EUR = {f.eur_to_chf(euros=euros):.2f} CHF')
print()


""" 11.	Napravite funkciju koja od korisnika traži da unese neki negativni broj  i onda taj broj pretvara u pozitivni!
"""
negative_number = int(input("Unesite jedan negativni broj: "))
print(f'Pozitivan broj: {f.to_positive_number(negative_number)}')
print()



""" 12.	Napravite vlastitu funkciju za obračun plaće.
        a. Od vas se traži da unesete broj redovnih dana bez bolovanja u mjesec dana, broj dana na bolovanju u mjesec dana i iznos dnevnice
        b. U funkciji koju zovete, izračunajte iznos koji dobijete za broj dana na bolovanju i dnevnicu koja iznosi 0,8 redovne dnevnice. 
            Vrijednost vraćate
        c. U glavnom tijelu programa računate redovna primanja i zbrajate ih sa iznosom primanja iz funkcije za bolovanje
        d. Ispišite plaću za taj mjesec.
 """
dnevnica = 20.00
redovni_dani = 15
dani_na_bolovanju = 5

primanja_na_bolovanju = f.izracun_primanja_na_bolovanju(dani_bolovanje=dani_na_bolovanju, dnevnica=dnevnica)
isplata = (redovni_dani * dnevnica) + primanja_na_bolovanju
print(f"Ukupna placa iznosi: {isplata:.2f} EUR")










