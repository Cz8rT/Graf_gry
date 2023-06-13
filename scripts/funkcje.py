from termcolor import colored  # Kolorowanie tekstu w konsoli


def Hello_Screen():  # Funkcja wypisująca ekran powitalny
    print(colored("\n* * * * * * * * * * * * *", 'yellow'))
    print(colored(f'{"*": <24}*', 'yellow'))
    print(colored(f'{"*": <5}', 'yellow'),
          colored(f'Zagrajmy w 21!', 'green', attrs=["bold"]), colored(f'{"*": >4}', 'yellow'))
    print(colored(f'{"*": <24}*', 'yellow'))
    print(colored("*", 'yellow'),
          colored("Jestem Antagonistą...", 'red'), colored("*", 'yellow'))
    print(colored("*", 'yellow'),
          colored("...i zawsze wygrywam!", 'red'), colored("*", 'yellow'))
    print(colored(f'{"*": <24}*', 'yellow'))
    print(colored("* * * * * * * * * * * * *\n", 'yellow'))


def Nastepny_Gracz(gracz):  # Funkcja zamieniająca aktywnego gracza
    if (gracz == "Protagonista"):
        return "Antagonista"
    else:
        return "Protagonista"


def Wyswietl_Stan(wynik, aktywnyGracz):    # Funkcja wyświetlająca aktualny stan gry
    print("Wynik:", colored(f'{wynik}', 'blue'))
    color = "red"
    if (aktywnyGracz == "Protagonista"):
        color = "green"
    print("Aktualny gracz:", colored(f'{aktywnyGracz}', color))


def Wybierz_Ruch():  # Funkcja sprawdzająca poprawność wprowadzonej przez protagonistę liczby
    while True:
        try:
            number = int(
                input("Protagonisto podaj swój wybór ('4','5','6'): "))
            if (number != 4 and number != 5 and number != 6):
                print("Wybierz liczbę 4, 5 lub 6!\n")
                continue
            print()
            return number
        except ValueError:
            print("Podano nieprawidłową wartość!\n")
