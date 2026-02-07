import pygame
import random
import sys

pygame.init()

# Ustawienia okna
szerokosc, wysokosc = 600, 400
okno = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Zgadnij liczbę - Gra")

# Kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
zielony = (0, 200, 0)
czerwony = (200, 0, 0)
niebieski = (0, 0, 200)
zolty = (255, 255, 0)

# Czcionka
czcionka = pygame.font.Font(None, 36)

# Ustawienia gry
liczba_rund = 3
punkty = 0

for runda in range(1, liczba_rund + 1):
    tajna_liczba = random.randint(1, 10)
    proby = 0
    wygrana = False

    # Przyciski
    przyciski = []
    for i in range(1, 11):
        rect = pygame.Rect(30 + (i-1)*50, 300, 40, 40)
        przyciski.append((i, rect))

    # Pętla rundy
    running = True
    while running:
        okno.fill(bialy)

        # Instrukcja
        tekst = czcionka.render(f"Runda {runda}/{liczba_rund} - Kliknij liczbę 1–10", True, czarny)
        okno.blit(tekst, (80, 50))

        # Rysowanie przycisków
        for numer, rect in przyciski:
            kolor = niebieski if not wygrana else zielony
            pygame.draw.rect(okno, kolor, rect)
            txt = czcionka.render(str(numer), True, zolty)
            okno.blit(txt, (rect.x+10, rect.y+5))

        # Komunikat po trafieniu
        if wygrana:
            msg = czcionka.render(f"Brawo! Zgadłeś w {proby} próbach", True, czerwony)
            okno.blit(msg, (150, 150))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not wygrana:
                pos = pygame.mouse.get_pos()
                for numer, rect in przyciski:
                    if rect.collidepoint(pos):
                        proby += 1
                        if numer == tajna_liczba:
                            wygrana = True
                            punkty += max(0, 10 - proby + 1)
                        elif numer < tajna_liczba:
                            print("Za mało!")
                        else:
                            print("Za dużo!")

pygame.quit()
print(f"Koniec gry! Zdobyłeś {punkty} punktów w {liczba_rund} rundach.")
sys.exit()
