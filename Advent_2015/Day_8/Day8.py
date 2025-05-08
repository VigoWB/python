from Advent_2015.scaffolding.utils import splitLines

def wczytaj():
    linia = splitLines('Day8_input.txt')
    return linia

def wykonaj(linia: str)->tuple[int, int]:
    tekst = linia
    znaki = 0
    litery = 0
    for linia in tekst:
        print(linia, len(linia))
        for znak in linia:
            if '\\' in linia:
                continue
            print(znak)
            znaki += 1
        # znaki += len(linia)
        # litery += sum(c.isalpha() for c in linia)

        # if 'c' in linia:
        #     if linia.index('c') + 2 < len(linia):
        #         print(ord('\\'), format(ord('\\'), '08b')) # kod ASCII i konwersja na 8-bitowy binarny string
        #         print(f"",linia[linia.index('c') + 2])
        #     if linia.index('c') + 2 >= len(linia):
        #         print('za dlugie')
    return znaki, litery

def main():
    wczytaj()
    print(wykonaj(wczytaj()))

if __name__ == '__main__':
    main()