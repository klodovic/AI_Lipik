"""
1. zadatak
Stvorite Numpy ndarray objekt iz Python liste dimenzija 2x3. Elemente polja definirajte
proizvoljno. Ispišite ga na ekran. Provjerite tip podataka koje pohranjuje i dimenzije.
"""

import numpy as np

np_lista = np.array([[10, 20, 30], [40, 50, 60]])

print("2D Numpy polje:\n", np_lista)

print(np_lista.dtype)
print(np_lista.shape)

"""
2. zadatak
Stvorite Numpy ndarray objekt nasumičnih brojeva veličine 3x4x2. Za generiranje nasumičnih
brojeva koristite odgovarajuću Numpy funkciju. Tip elemenata Numpy polja mora biti
numpy.float64.
Ispišite na ekran:
● Broj osi
● Dimenzije polja
● Broj elemenata u polju
● Tip elemenata u polju
"""
print("\nDrugi zadatak:")
np.random.seed(0)
np_nasumicno = np.random.rand(3, 4, 2).astype(np.float64)
print(np_nasumicno.ndim)
print(np_nasumicno.shape)
print(np_nasumicno.size)
print(np_nasumicno.dtype)

print(np_nasumicno)

"""
3. zadatak
Kopirajte Numpy polje iz prethodnog zadatka, te novom polju promijenite tip u np.int16, te ispišite
novi tip polja.
"""

print("\nTreci zadatak:")
np_int16 = np_nasumicno.astype(np.int16)
print(np_int16.dtype)

"""
4. zadatak
Stvorite 2x7x3 Numpy polje tipa numpy.int32 čiji svi elementi imaju vrijednost 9. Osim pristupa
kojeg ste koristili, postoji li neki alternativni način kreiranja ovakvog polja?
"""

np_nasumicno = np.full((2, 7, 3), 9, dtype=np.int32)
print(np_nasumicno)

"""
5. zadatak
Koristeći odgovarajuću Numpy funkciju, Stvorite Numpy polje koje sadrži svaki treći cjelobrojni
broj u rasponu [3, 15>.
"""
np_treci = np.arange(3, 15, 3)
print(np_treci)

"""
6. zadatak
Koristeći odgovarajuću Numpy funkciju, stvorite Numpy polje koji sadrži 12 jednoliko raspoređenih
brojeva u rasponu [2, 19].
"""
np_jednoliko = np.linspace(2, 19, 12)
print(np_jednoliko)

"""
7. zadatak
Stvorite jediničnu matricu dimenzije 4x4, te još jednu matricu istih dimenzija čiji svi elementi imaju
vrijednost 9. Ispišite na ekran za ove dvije matrice:
● Zbroj
● Razliku
● Umnožak (element po element)
● Količnik
"""
jedinicna_matrica = np.eye(4)
matrica_9 = np.full((4, 4), 9)

zbroj = jedinicna_matrica + matrica_9
print("Zbroj:\n", zbroj)
razlika = matrica_9 - jedinicna_matrica
print("Razlika:\n", razlika)
umnozak = jedinicna_matrica * matrica_9
print("Umnožak:\n", umnozak)
kolicnik = matrica_9 / jedinicna_matrica
print("Količnik:\n", kolicnik)

"""
8. zadatak
Stvorite 1D ndarray od 10 elemenata proizvoljnih vrijednosti. Bez korištenja for petlje postavite
svaki drugi element u rasponu indeksa [2, 7> na vrijednost 99.
"""
np_1d = np.array([5, 12, 7, 3, 8, 15, 22, 9, 4, 11])
np_1d[2:7:2] = 99
print(np_1d)

"""
9. zadatak
Stvorite 2D ndarray dimenzija 5x6 nasumičnih vrijednosti. Bez korištenja for petlje izdvojite svaki
drugi stupac u zasebnu varijablu. Također, u zasebnu varijablu izdvojite posljednja 3 retka.
Provjerite dijele novo kreirane varijable memoriju s izvornim nizom?
"""
print("\nDeveti zadatak:")
np_2d = np.random.randint(0, 10, (5, 6))
print(np_2d)
svaki_drugi_stupac = np_2d[:, ::2]
zadnja_tri_retka = np_2d[-3:, :]

print("Svaki drugi stupac:\n", svaki_drugi_stupac)
print("Zadnja tri retka:\n", zadnja_tri_retka)
print(np.shares_memory(np_2d, svaki_drugi_stupac))

"""
10. zadatak
Stvorite 2D Numpy polje dimenzija 16x16 koje ima vrijednosti od 1 do 256. Stvorite novo Numpy
polje koje sadrži iste elemente prvog polja, ali u obliku 4x8x8. Koja Numpy funkcija je prigodna
kako bi se ovo ostvarilo? Vizualizirajte oblik novog ndarray-a. Dovoljna je skica na papiru ili skica
u nekom digitalnom alatu.
"""
print("\nDeseti zadatak:")
np_2d = np.random.randint(1, 256, (16, 16))
print(np_2d)
np_reshaped = np_2d.reshape(4, 8, 8)
print(np_reshaped)
print(np_reshaped.shape)


"""
11. zadatak
Stvorite 3D Numpy polje dimenzija 3x576x720. Stvorite novo Numpy polje koje sadrži iste
elemente prvog polja, ali u obliku 576x720x3. Koja Numpy funkcija je prigodna kako bi se ovo
ostvarilo?
"""

np_3d = np.random.rand(3, 576, 720)
np_transponse = np.transpose(np_3d, (1, 2, 0))



"""
12. zadatak
Stvorite 2D Numpy polje dimenzija 2x3. Ukoliko je srednja vrijednost svih elemenata veća od 10
ispišite sumu svih elemenata, u suprotnom ispišite vrijednost najvećeg elementa u polju.
"""


np_2d_12 = np.random.randint(0, 20, (2, 3))
np_mean = np_2d_12.mean()
if np_mean > 10:
    print(f'Suma svih elemenata: {np_2d_12.sum()}')
else:
    print(f'Najveći element u polju: {np_2d_12.max()}')


