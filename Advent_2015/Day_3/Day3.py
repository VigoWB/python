from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def pozycje():
    plik = loadFile("Day3_input.txt")
    mapa = {}
    pozycja = (0, 0)
    mapa[pozycja] = 0
    for znaczek in plik:
        ruch = kierunek(znaczek)
        #print(ruch, pozycja)
        pozycja = (pozycja[0] + ruch[0], pozycja[1] + ruch[1])
        mapa[pozycja] = mapa.get(pozycja, 0) +1
    return mapa


def ile_domow():
    zbior = pozycje()
    policzone_domy = 1
    for klucz, wartosc in zbior.items():
        if wartosc >= 1:
            policzone_domy += 1
    return policzone_domy

def kierunek(kierunek: str) -> (int, int):
    if kierunek == ">":
        return 1, 0
    if kierunek == "<":
        return -1, 0
    if kierunek == "^":
        return 0, 1
    if kierunek == "v":
        return 0, -1


def main():
    print(ile_domow())
    #print(pozycje())
    # print(kierunek())


if __name__ == '__main__':
    main()