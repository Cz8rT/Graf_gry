from termcolor import colored  # Kolorowanie tekstu w konsoli
from scripts.funkcje import Hello_Screen, Wyswietl_Stan, Wybierz_Ruch, Nastepny_Gracz
from scripts.MinMax import MinMax

score = 0  # Początkowy wynik gry
currentPlayer = "Protagonista"  # Początkowy gracz
end = False  # Warunek końca gry

# Ekran powitalny
Hello_Screen()


class Wybor:               # Pomocnicza struktura służąca połączeniu wybranego ruchu...
    def __init__(self):    # ...z wyliczoną dla tego ruchu wartością przez algorytm MinMax()
        self.wartosc = 1000
        self.ruch = 4


# Główna pętla programu
while not end:
    Wyswietl_Stan(score, currentPlayer)
    if (currentPlayer == "Protagonista"):  # Tura Protagonisty
        score += Wybierz_Ruch()
    else:
        print("Antagonista myśli...")  # Tura Antagonisty
        wybor = Wybor()
        for ruch_antagonisty in (4, 5, 6):  # Rozpatrywanie możliwych ruchów
            new_state = score + ruch_antagonisty
            # Wywołanie MinMax() dla nowego potencjalnego stanu
            res = MinMax(new_state, "Protagonista")
            print(
                f"Jeśli wybiorę {ruch_antagonisty} (z {score} na {new_state}) siła ruchu wyniesie: {res}")
            if (res < wybor.wartosc):  # Wybranie lepszego rozwiązania z możliwych ruchów
                wybor.wartosc = res
                wybor.ruch = ruch_antagonisty
        print("Wybieram:", wybor.ruch, "\n")
        score += wybor.ruch  # Przypisanie wybranej wartości do wyniku
    if (score >= 21):  # Sprawdzenie końca gry
        print(colored("***** Koniec gry! *****", 'yellow', attrs=["bold"]))
        print("Końcowy wynik", colored(score, 'blue'))
        if (score == 21):
            print("Pojedynek zakończył się remisem!")
        else:
            currentPlayer = Nastepny_Gracz(currentPlayer)
            color = "red"
            if (currentPlayer == "Protagonista"):
                color = "green"
            print("Pojedynek wygrał", colored(f'{currentPlayer}', color))
            print("Gratulacje!")

        # ******************* Czy chcemy zagrać ponownie? ****************
        print("\nCzy chcesz zagrać ponownie?")
        answer = str(input("...choć i tak nie masz szans (T/N): "))
        if (answer.capitalize() != "T"):
            end = True
        else:
            print(colored("\n***** Zagrajmy ponownie! *****",
                  'magenta', attrs=["bold"]))
            score = 0
            currentPlayer = "Antagonista"
        # ****************************************************************

    currentPlayer = Nastepny_Gracz(currentPlayer)

input("\nNaciśnij Enter, by zakończyć...")
