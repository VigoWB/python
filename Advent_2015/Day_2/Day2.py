from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def ile_kartonow():
    plik = splitLines("Day2_input.txt")
    suma = 0
    for linijka in plik:
        szer, wys, gleb = [int(opz) for opz in linijka.split('x')]
        zapas = min((szer*wys),(wys*gleb),(gleb*szer))
        liczenie = (szer*wys+wys*gleb+gleb*szer)*2
        suma += liczenie + zapas
    return suma

def main():
    print(ile_kartonow())

if __name__ == '__main__':
    main()