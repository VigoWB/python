from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    # linia = splitLines('Day8_input.txt')
    linia = splitLines('test.txt')
    return linia

def wykonaj(linia: str)->tuple[int, int]:
    tekst = linia
    litery = 0
    for linia in tekst:
        res = policz(linia[1:-1])
        litery += len(linia)
        # print(linia, len(linia), res)
    return res, litery



def policz(linia: str)->int:
    znaki = 0
    for pozycja, znak in enumerate(linia):
        if znak == '\\':
            if isescape(linia[pozycja:pozycja + 4]):
                print(f"test ZDANy ", linia)
                znaki += 4
                # print(isescape(linia[pozycja:pozycja+4]))
            continue
        znaki += 1
    return znaki

def isescape(linia: str) -> bool:
    print(f'TESTY LINI: ', linia)
    if linia[0] == '\\' and linia[1] == 'x' and len(linia) == 4:
        # if linia[-2] == znak in range(0,9) and linia[-1] == range('a-f'):
        hex_digits = '0123456789abcdefABCDEF' # sciagnolem z AI
        return linia[2] in hex_digits and linia[3] in hex_digits
    else:
        return False



def main():
    wczytaj()
    print(wykonaj(wczytaj()))

if __name__ == '__main__':
    main()