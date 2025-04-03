from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def pozycje():
    plik = loadFile("Day3_input.txt")
    mapa = {}
    mapa[(0,0)] = 1
    #print(mapa[(0,1)])
    for znaczek in plik:
        #kierunek = znaczek.split()
        if znaczek in plik == ">":
            mapa[(0,+1)]
            if krok in mapa:
                mapa[krok] = 1
            else:
                mapa[krok] += 1

        if znaczek in plik == "^":
            mapa[(+1,0)]
            if krok in mapa:
                mapa[krok] = 1
            else:
                mapa[krok] += 1

    return mapa


def main():
    print(pozycje())



if __name__ == '__main__':
    main()