from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day9_input.txt')
    return linia

def wykonaj(linia: str)->tuple[int, int]:
    tekst = linia
    litery = 0
    res = 0
    for linia in tekst:

        res += len(linia)
        tlitery = len(linia)
        litery += tlitery
        print(linia, tlitery)
        # print(linia, len(linia), res)
    return res, litery






def main():
    print(wczytaj())



if __name__ == '__main__':
    main()