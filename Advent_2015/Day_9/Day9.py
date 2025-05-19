from Advent_2015.scaffolding.utils import splitLines
from Advent_2015.Day_9.klasaDay_9 import Mapki, Kombinator


def wczytaj() -> tuple[dict, Mapki]:
    surowe_dane = splitLines('Day9_input.txt')
    # przeksztalc wczytane linie na dane (slownik tupli str, str int)
    dane = podzial(surowe_dane)
    # pusty obiekt miasta
    miasta = Mapki()

    # klucz to tupla (str, str)
    for klucz in dane.keys():
        # z racji tego ze nie musimy sie przejmowac niczym mozemy dodac oba miasta
        # bo klasa miasta dba o spojnosc tych danych
        miasta.dodaj(klucz[0])
        miasta.dodaj(klucz[1])
    # zamiast zwracac surowa kolekcje elementow zwracam dane i slownik miast
    return dane, miasta


# def wykonaj(linie: list[str]) -> dict[str, int]:
#     miasta = {}
#     numer = 1
#     for linia in linie:
#         dane = podzial(linia)
#         for (skad, dokad) in dane.keys():
#             if skad not in miasta:
#                 miasta[skad] = numer
#                 numer += 1
#             if dokad not in miasta:
#                 miasta[dokad] = numer
#                 numer += 1
#     return miasta


def podzial(linie: list[str]) -> dict:
    slownik = {}
    for wpis in linie:
        wynik = wpis.split()
        slownik[(wynik[0], wynik[2])] = int(wynik[-1])
        slownik[(wynik[2], wynik[0])] = int(wynik[-1])
    return slownik


def main():
    wczytane = wczytaj()
    print("Miasta i ich numery:", wczytane)

    kombinuje = Kombinator([x for x in range(8)])
    print(f'sddas', kombinuje)


if __name__ == '__main__':
    main()
