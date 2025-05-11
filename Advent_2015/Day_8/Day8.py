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
        # print(linia, len(linia), res)
    return res, litery



def policz(linia: str)->int:
    znaki = 0
    for pozycja, znak in enumerate(linia):
        if znak == '\\':
            if isescape(linia[pozycja:pozycja+4]) == True:
                print(f"test ZDANy ", linia)
                # print(isescape(linia[pozycja:pozycja+4]))
            continue
        znaki += 1
    return znaki

def isescape(linia: str) -> bool:
    print(f'TESTY LINI: ', linia)
    if linia[0] == '\\' and linia[1] == 'x' and len(linia) == 4:
         # if linia[:-1] == 0:
        if linia[-2] == znak in range(0,9) and linia[-1] == range('a-f'):
            return True
    else:
        return False

        # if 'c' in linia:
        #     if linia.index('c') + 2 < len(linia):
        #         print(ord('\\'), format(ord('\\'), '08b')) # kod ASCII i konwersja na 8-bitowy binarny string
        #         print(f"",linia[linia.index('c') + 2])
        #     if linia.index('c') + 2 >= len(linia):
        #         print('za dlugie')


def main():
    wczytaj()
    print(wykonaj(wczytaj()))

if __name__ == '__main__':
    main()