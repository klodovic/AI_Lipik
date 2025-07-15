import math

def hello():
    print("Hello world")
    print("AI centar Lipik")
    
def ljetovanje():
    broj_dana = 10
    cijena = 130.99
    print(f'Cijena ljetovanja iznosi: {broj_dana * cijena}')
    
def favorite_book(title):
    print(f'Jedna od mojih najdrazih knjiga je {title}')
    
def auti(marka, zemlja_porijekla):
    print("Moj najdrazi auto je " + marka)
    print("Zemlja_porijekla: " + zemlja_porijekla)

def informacije(ime, prezime, godina_rodjenja):
    print(f'Prezime i ime korisnika: {prezime.title() + " " + ime.title()}')
    print(f'Godina rodjenja: {godina_rodjenja}') 
    
def nadimak(nadimak_korisnika):
    print("Pozdrav, " + nadimak_korisnika)
    
def fav_movie(movie, actor):
    print(f'Vaš omiljeni film je {movie}, u kome glumi {actor}!')

def fav_town_country(town, country):
    print(f'{town} i {country} su prekrasni za posjetiti u ovo doba godine...')

def kvadratura(sirina, duljina):
    return sirina * duljina

def km_to_miles(kilometers):
    CONVERSION_FACTOR = 0.62137
    return kilometers * CONVERSION_FACTOR

def kvadrat(stranica):
    return pow(stranica, 2)

def trosak_goriva(litara_goriva, cijena_goriva = 1.5):
    return litara_goriva * cijena_goriva



