from Advent_2015.scaffolding.utils import splitLines
from Advent_2015.Day_9.klasaDay_9 import mapki

def wczytaj():
    linia = splitLines('Day9_input.txt')
    return linia

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

    print(wykonaj(wczytaj()))



if __name__ == '__main__':
    main()