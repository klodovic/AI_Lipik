def zbrajanje (a,b):
    return a + b

print ("Dobro došli jednostavnu kalkulator aplikaciju")

while True:
    print ("Za zbrajanje dva broja, unesite riječ 'zbrajanje")
    print ("Upišite 'quit' ako želite završiti")
    odgovor = input ("Vaš odgovor: ")
   
    if odgovor == "quit":
        print ("Zahvaljujem na korištenju")
        break
    if odgovor == "zbrajanje":
        broj1 = float(input("Unesite prvi broj"))
        broj2 = float(input("Unesite drugi broj"))
        rezultat = zbrajanje (broj1, broj2)
        print ("Zbroj vaša dva broja glasi:", rezultat)
       
print ("kaj programa")
