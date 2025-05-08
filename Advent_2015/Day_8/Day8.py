from Advent_2015.scaffolding.utils import splitLines

def wykonaj():
    tekst = splitLines('Day8_input.txt')
    znaki = 0
    litery = 0
    for linia in tekst:
        print(linia, len(linia))
        # znaki += len(linia)
        # litery += sum(c.isalpha() for c in linia)

        # if 'c' in linia:
        #     if linia.index('c') + 2 < len(linia):
        #         print(ord('\\'), format(ord('\\'), '08b')) # kod ASCII i konwersja na 8-bitowy binarny string
        #         print(f"",linia[linia.index('c') + 2])
        #     if linia.index('c') + 2 >= len(linia):
        #         print('za dlugie')
    return

def main():
    # print(wczytaj())
    print(wykonaj())

if __name__ == '__main__':
    main()