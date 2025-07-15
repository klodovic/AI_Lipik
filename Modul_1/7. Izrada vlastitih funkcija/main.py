#functions
import func

#main
print("Trla baba lan da joj prode dan....")


func.hello()       
         
func.ljetovanje()  
print()

func.favorite_book("Hobbit") 
print()

func.auti("BMW", "Njemacka")
print()

func.informacije("Pero", "Peric", 2020)
print()

nadimak = input("Unesite svoje nadimak: ")
func.nadimak(nadimak)
print()

movie_title = input("Unesite naziv omiljenog filma: ")
actor_name = input("Unesite ime svog omiljenog glumca ili glumice: ")
func.fav_movie(movie_title, actor_name)
print()

town = input("Unesite naziv grada: ")
country = input("Unesite naziv zemlje: ")
func.fav_town_country(town=town, country=country)
print()


#with return value
sirina = 7.5
duljina = 5.0
print(func.kvadratura(sirina=sirina, duljina=duljina))

converted = func.km_to_miles(157)
print(converted)
print()

stranica = 2
print(func.kvadrat(stranica))
print()

litara_goriva = 20.2
cijena_goriva = 1.45
two_param = func.trosak_goriva(litara_goriva, cijena_goriva)
one_param = func.trosak_goriva(litara_goriva)
print(two_param)
print(one_param)


















