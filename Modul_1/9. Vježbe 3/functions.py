#1
def greeting():
    print("Dobro jutro....")
    
#2
def sport(sport, player):
    print(f'{player} i {sport}, sto pozeljeti vise!')

#3
def pozivnica(uzvanik, mjesto):
    print(f'Postovani/a {uzvanik}')
    print(f'Pozivamo vas na svecani domjenak 20 12. u {mjesto}.')

#4
def filmovi(movie, gerne):
    print(f'Danas, filmska vecer, {gerne} {movie}.')

#5
def difference_number(x, y):
    return abs(x - y)

#6
def konverzija(kunas, exchange_rate=7.53450):
    return kunas / exchange_rate

#7
def lower_letters(text):
    return text.lower()

#8
def prosjecna_brzina(distance, time):
    return distance / time

#9
def number_division(x, y):
    integer = x // y
    remainder = x % y
    return integer, remainder

#10
def eur_to_chf(euros, exchange_rate=0.94):
    return euros * exchange_rate

#11
def to_positive_number(number):
    return abs(number)

#12
def izracun_primanja_na_bolovanju(dani_bolovanje, dnevnica):
    return dani_bolovanje * (dnevnica * 0.8)









