from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day8_input.txt')
    # linia = splitLines('test.txt')
    return linia

def wykonaj(linia: str)->tuple[int, int]:
    tekst = linia
    litery = 0
    res = 0
    for linia in tekst:
        tres = policz(linia[1:-1])# pierwsza czesc zadania
        res += tres
        tlitery = len(linia)
        litery += tlitery
        print(linia, tlitery, tres)
        # print(linia, len(linia), res)
    return res, litery






def main():
    wczytaj()
    res, litery = wykonajdwa(wczytaj())
    print(res - litery)

if __name__ == '__main__':
    main()