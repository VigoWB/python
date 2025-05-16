from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day9_input.txt')
    return linia

def wykonaj(linie: str):
    tekst = linie
    miasta = {}

    for linie in tekst:
        dane = podzial(linie)
        for asd in dane:
            numer = len(miasta)
            miasta[asd[0]] = numer + 1
            if miasta[asd[0]] == miasta.keys():
                return
            else:
                miasta[asd[0]] = numer + 1


    print(len(miasta),miasta)
    return

def podzial(linie: list[str])->dict[tuple[str, str], int]:
    polaczenia ={}
    miasta = {}
    linia = linie.split()
    for slowa in linia:
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