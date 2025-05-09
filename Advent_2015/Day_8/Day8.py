from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day8_input.txt')
    return linia

def wykonaj(linia: str)->tuple[int, int]:
    tekst = linia
    litery = 0
    for linia in tekst:
        res = policz(linia)
        print(linia, len(linia), res)
    return res, litery



def policz(linia: str)->int:
    znaki = 0
    for znak in linia[1:-1]:
        if znak == '\\':
            if znak in linia[+1] == 'x':
                print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
            continue
        znaki += 1


        # if 'c' in linia:
        #     if linia.index('c') + 2 < len(linia):
        #         print(ord('\\'), format(ord('\\'), '08b')) # kod ASCII i konwersja na 8-bitowy binarny string
        #         print(f"",linia[linia.index('c') + 2])
        #     if linia.index('c') + 2 >= len(linia):
        #         print('za dlugie')
    return znaki

def main():
    wczytaj()
    print(wykonaj(wczytaj()))

if __name__ == '__main__':
    main()