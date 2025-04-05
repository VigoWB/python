from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def pozycje():
    plik = loadFile("Day3_input.txt")
    mapa = {}
    mapa[(0,0)] = 1
    #print(mapa[(0,1)])
    for znaczek in plik:
        ruch = kierunek(znaczek)
        if ruch in mapa.keys():
            mapa[(ruch)] += 1
        else:
            mapa[(ruch)] = 1
    return mapa

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
    print(pozycje())
    print(kierunek())



if __name__ == '__main__':
    main()