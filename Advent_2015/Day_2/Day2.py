from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines


def ile_kartonow():
    plik = splitLines("Day2_input.txt")
    for linijka in plik:
        linia_mnozenie = linijka.split('x')
        for najmniejszy in linia_mnozenie:
            print(najmniejszy, min(najmniejszy))

    return


def main():
    print(ile_kartonow())

if __name__ == '__main__':
    main()