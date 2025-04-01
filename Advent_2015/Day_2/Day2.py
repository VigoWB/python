from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines


def ile_kartonow():
    plik = splitLines("Day2_input.txt")
    for linijka in plik:
        szer, wys, gleb = [int(opz) for opz in linijka.split('x')]
        zapas = min(szer, wys, gleb)
        zapas2 = min((szer*wys),(wys*gleb),(gleb*szer))
        liczenie = szer*wys+wys*gleb+gleb*szer
        print(liczenie*2 + zapas2)
    return


def main():
    print(ile_kartonow())

if __name__ == '__main__':
    main()