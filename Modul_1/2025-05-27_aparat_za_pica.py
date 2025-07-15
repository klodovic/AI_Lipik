import os

aparat = {
    "kava": {
        "ime": "Kava",
        "cijena": 1.5,
        "dostupno": True
    },
    "čaj": {
        "ime": "Čaj",
        "cijena": 1.2,
        "dostupno": False
    },
    "sok": {
        "ime": "Sok",
        "cijena": 2.0,
        "dostupno": False
    },
    "voda": {
        "ime": "Voda",
        "cijena": 1.0,
        "dostupno": True
    }
}

def ispis_izbornika():
    count = 1
    os.system("clear")  # Za Windows koristiti cls
    print("------------------------------------")
    print("Naš menu")
    print("------------------------------------")
    for key in aparat:
        print(f"\t{count}.{aparat[key]["ime"]}")
        count += 1
    print("------------------------------------")

while True:
    ispis_izbornika()
    odabir = input("Unesite željeno piće (Kava, Čaj, Sok, Voda) ili 'izlaz' za prekid:").lower()

    if odabir == "izlaz":
        print("Hvala na korištenju Virtualnog Aparata za Pića!")
        break
    else:
        if odabir not in aparat.keys():
            print("Nevaljan odabir. Molimo odaberite piće s menija.")
        else:
            if aparat[odabir]["dostupno"]:
                print("Izabrali ste", aparat[odabir]["ime"], "Cijena:", aparat[odabir]["cijena"], " EUR. Uživajte!")
            else:
                print("Izabrali ste", aparat[odabir]["ime"], ". Trenutno nije dostupan. Molimo odaberite drugo piće.")
    input("") # Ovo čeka prije čišćenja ekrana