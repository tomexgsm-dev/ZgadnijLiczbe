

import random

def gra_rundy(liczba_rund=3):
    punkty = 0
    print("Witaj w grze 'Zgadnij liczbę'!")
    print(f"Masz {liczba_rund} rund, żeby zdobyć jak najwięcej punktów.")

    for runda in range(1, liczba_rund + 1):
        tajna_liczba = random.randint(1, 10)
        proby = 0
        print(f"\nRunda {runda}: Zgadnij liczbę od 1 do 10.")

        while True:
            str_input = input("Podaj liczbę: ")
            if not str_input.isdigit():
                print("Proszę podaj prawidłową liczbę.")
                continue

            liczba = int(str_input)
            proby += 1

            if liczba < tajna_liczba:
                print("Za mało!")
            elif liczba > tajna_liczba:
                print("Za dużo!")
            else:
                print(f"Brawo! Zgadłeś liczbę {tajna_liczba} w {proby} próbach!")
                punkty += max(0, 10 - proby + 1)
                break

    print(f"\nKoniec gry! Zdobyłeś {punkty} punktów w {liczba_rund} rundach.")

# Uruchomienie gry
gra_rundy(3)
