import os

################ class definition for terminal colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


################ constants
QUEUE_MAX = 3
LIST_IS_FULL = "Pokusajte ponovno kasnije. Red je pun!!!"
NO_CLIENTS_IN_THE_LIST = "Lista cekanja je prazna. Dodajte novog klijenta!"
GOODBYE_MESSAGE = "Hvala sto se koristili nasu aplikaciju...."


################ empty list
queue = []


################ function definitions
def menu():
    print("------------------------------------------")
    print("GLAVNI IZBORNIK")
    print(" \t1. Dodaj klijenta u red \n\t2. Prikazi trenutni red cekanja \n\t3. Pozovi sljedeceg klijenta \n\t0. Izlaz iz programa")
    print("------------------------------------------")

def warning_message(message):
    print(f"{bcolors.WARNING}{message}{bcolors.ENDC}")
    
def info_message(message):
    print(f"{bcolors.OKBLUE}{message}{bcolors.ENDC}")
    
def error_message():
    print(f"{bcolors.FAIL}Pogresan unos. Unesite jedan od ponudenih brojava iz menija!!{bcolors.ENDC}")

def insert_new_client(client):
    queue.append(client)
    print(f'{bcolors.OKGREEN}Uspjesno ste dodali klijenta/icu "{client}" u listu cekanja!!!{bcolors.ENDC}')

def print_clients_in_list(queue):
    print(f'{bcolors.WARNING}Klijenti u listi cekanja:{bcolors.ENDC}')
    i = 1
    for q in queue:
        print(f'\t{bcolors.OKCYAN}{i}. {q}{bcolors.ENDC}')
        i = i + 1
    print(f'{bcolors.OKGREEN}Broj slobodnih mjesta za klijente:  {QUEUE_MAX - len(queue)}{bcolors.ENDC}')

def client_to_call(queue):
    first_client = queue[0]
    queue.pop(0)
    print(f'{bcolors.OKCYAN}Klijent "{first_client}" je pozvan/a. {bcolors.ENDC}')
    
def clear_terminal():
    input(f'{bcolors.BOLD}{bcolors.FAIL}\nPritisnite Enter za nastavak...{bcolors.ENDC}')
    os.system('cls' if os.name == 'nt' else 'clear')


################ main program
while True:
    menu()
    
    try:
        user_choice = int(input("Odaberite jednu od akcija iz menija unosom broja od 0 do 3: "))
        
        if user_choice < 0 or user_choice > 3:
            error_message()
            clear_terminal()
    
        #main operations
        if user_choice == 1: 
            client = input("Unesite ime klijenta/ce: ")
            if len(queue) >= QUEUE_MAX:
                info_message(LIST_IS_FULL)
                clear_terminal()
            if queue == [] or len(queue) < QUEUE_MAX:
                insert_new_client(client=client)
                clear_terminal()
                
        elif user_choice == 2:
            if queue == []:
                warning_message(NO_CLIENTS_IN_THE_LIST)
                clear_terminal()
            else:
                print_clients_in_list(queue=queue)
                clear_terminal()
                    
        elif user_choice == 3:
            if queue == []:
                warning_message(NO_CLIENTS_IN_THE_LIST)
                clear_terminal()
            else: 
                client_to_call(queue=queue)
                clear_terminal()
                
        elif user_choice == 0:
            info_message(GOODBYE_MESSAGE)
            break
    
    except ValueError:
        print(f'{bcolors.FAIL}To nije broj. Pokusajte ponovno.{bcolors.ENDC}')
        clear_terminal()
        

























