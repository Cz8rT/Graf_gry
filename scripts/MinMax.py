def MinMax(stan, gracz):
    # Węzeł spełniający warunek końca gry
    if (stan == 21):
        return 0  # Remisowy węzeł
    if (stan > 21):
        if (gracz == "Protagonista"):
            return (stan - 21)  # Wynik na plus
        else:
            return (21 - stan)  # Wynik na minus

    mozliwe_ruchy = [
        stan + ruch for ruch in (4, 5, 6)
    ]

    if (gracz == "Protagonista"):
        rezultaty = [   # Rozpatrzenie możliwych kolejnych zagrań jako Antagonista
            MinMax(nowy_stan, "Antagonista") for nowy_stan in mozliwe_ruchy
        ]
        return max(rezultaty)
    else:
        rezultaty = [   # Rozpatrzenie możliwych kolejnych zagrań jako Protagonista
            MinMax(nowy_stan, "Protagonista") for nowy_stan in mozliwe_ruchy
        ]
        return min(rezultaty)
