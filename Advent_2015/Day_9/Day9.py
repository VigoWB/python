from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day9_input.txt')
    return linia

def wykonaj(linia: str):
    tekst = linia
    for linia in tekst:
        dane = podzial(linia)
        print(dane)
    return

def podzial(linia: str)->tuple[str, str, int]:
    czesci = linia.split()
    for dane in czesci:
        zkad = czesci[0]
        dokad = czesci[2]
        odleglosc = czesci[-1]
    return zkad, dokad, odleglosc




def main():
    print(wykonaj(wczytaj()))



if __name__ == '__main__':
    main()