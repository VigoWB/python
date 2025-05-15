from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day9_input.txt')
    return linia

def wykonaj(linie: str):
    tekst = linie
    for linie in tekst:
        dane = podzial(linie)
        print(dane)
    return

def podzial(linie: list[str])->dict[tuple[str, str], int]:
    polaczenia ={}
    for linia in linie:
        linia = linie.split()
        zkad = linia[0]
        dokad = linia[2]
        odleglosc = int(linia[-1])
        polaczenia[(zkad, dokad)] = odleglosc
        polaczenia[(dokad, zkad)] = odleglosc
    return polaczenia




def main():
    print(wykonaj(wczytaj()))



if __name__ == '__main__':
    main()