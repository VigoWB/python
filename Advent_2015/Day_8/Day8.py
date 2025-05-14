from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    # linia = splitLines('Day8_input.txt')
    linia = splitLines('test.txt')
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


def wykonajdwa(linia: str)->tuple[int, int]:
    tekst = linia
    litery = 0
    res = 0
    for linia in tekst:
        tres = partdwa(linia)
        res += tres
        tlitery = len(linia)
        litery += tlitery
        print(linia, tlitery, tres)
        # print(linia, len(linia), res)
    return res, litery

def partdwa(linia: str) -> int:
    znaki = 0
    pozycja = 0
    while pozycja < len(linia):
        znak = linia[pozycja]
        if znak == '\"':
            if pozycja == len(linia) - 1:
                znaki += 3
                pozycja += 1
                continue
            if pozycja == len(linia) - len(linia):
                znaki += 3
                pozycja += 1
                continue
        if znak == '\\':
            if pozycja == linia[1:-1]:
                if pozycja + 1 == '\"':
                    znaki += 4
                    pozycja += 2
                else:
                    znaki += 1
                    pozycja += 1
                continue
        else:
            znaki += 1
            pozycja += 1

    return znaki


def policz(linia: str)->int:
    znaki = 0
    pozycja = 0
    while pozycja < len(linia):
        znak = linia[pozycja]
        if znak == '\\':
            if pozycja == len(linia) - 1:
                znaki += 1
                pozycja += 1
                continue
            if isescape(linia[pozycja:pozycja + 4]):
                znaki += 1
                pozycja += 4  # przeskocz 4 znaki, bo to sekwencja ucieczki \xNN
            else:
                if linia[pozycja + 1] in ["\\", "\""]:  # przeskocz 2 znaki, bo to np. \\ lub \"
                    znaki += 1
                    pozycja += 2
                else:
                    znaki += 1
                    pozycja += 1
        else:
            znaki += 1
            pozycja += 1
    return znaki



def isescape(linia: str) -> bool:
    if linia[1] != 'x':
        return False
    if len(linia) != 4:
        return False
    hex_digits = '0123456789abcdef'
    if str.lower(linia[2]) not in hex_digits:
        return False
    if str.lower(linia[3]) not in hex_digits:
        return False
    return True



def main():
    wczytaj()
    res, litery = wykonajdwa(wczytaj())
    print(litery - res)

if __name__ == '__main__':
    main()