from Advent_2015.scaffolding.utils import splitLines
from Advent_2015.Day_9.klasaDay_9 import Mapki

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

def wykonaj(linie: list[str]) -> dict[str, int]:
    miasta = {}
    numer = 1
    for linia in linie:
        dane = podzial(linia)
        for (skad, dokad) in dane.keys():
            if skad not in miasta:
                miasta[skad] = numer
                numer += 1
            if dokad not in miasta:
                miasta[dokad] = numer
                numer += 1
    return miasta

def podzial(linia: str) -> dict:
    slowa = linia.split()
    zkad = slowa[0]
    dokad = slowa[2]
    odleglosc = int(slowa[-1].lstrip('='))
    return {(zkad, dokad): odleglosc, (dokad, zkad): odleglosc}




def main():
    print("Miasta i ich numery przez funkcje:", wczytaj())







if __name__ == '__main__':
    main()