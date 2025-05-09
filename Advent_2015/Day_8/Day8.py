from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day8_input.txt')
    return linia



def wykonaj(linia: str)->tuple[int, int]:
    tekst = linia
    for linia in tekst:
        res = policz(linia)
        print(linia, len(linia), res)
    return 1, 1 #tu beda kiedys wyniki



def policz(linia: str)->int:
    znaki = 0
    for znak in linia[1:-1]:
        if znak == '\\':
            continue
        znaki += 1
    return znaki



def main():
    wczytaj()
    print(wykonaj(wczytaj()))

if __name__ == '__main__':
    main()