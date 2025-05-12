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
        tres = policz(linia[1:-1])
        res += tres
        tlitery = len(linia)
        litery += tlitery
        print(linia, tlitery, tres)
        # print(linia, len(linia), res)
    return res, litery



def policz(linia: str)->int:
    znaki = 0
    for pozycja, znak in enumerate(linia):
        if znak == '\\':
            if isescape(linia[pozycja:pozycja + 4]):
                # print(f"test ZDANy ", linia)
                znaki += 4
                # print(isescape(linia[pozycja:pozycja+4]))
            else:
                # print(f"test niezdany ", linia)
                znaki += 1
            continue
        if znak =='\n':
            print('tu jest N')
    return znaki

def isescape(linia: str) -> bool:
    if linia[-1] == '\\':
        return False
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
    print(wykonaj(wczytaj()))

if __name__ == '__main__':
    main()