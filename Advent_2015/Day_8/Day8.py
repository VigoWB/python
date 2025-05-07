from Advent_2015.scaffolding.utils import splitLines

def wykonaj():
    linijka = splitLines('Day8_input.txt')
    znaki = 0
    litery = 0
    for linia in linijka:
        znaki += len(linia)
        litery += sum(c.isalpha() for c in linia)
    return znaki, litery

def main():
    # print(wczytaj())
    print(wykonaj())

if __name__ == '__main__':
    main()