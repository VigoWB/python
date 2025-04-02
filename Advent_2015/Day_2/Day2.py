from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def ile_kartonow():
    plik = splitLines("Day2_input.txt")
    suma = 0
    for linijka in plik:
        szer, wys, gleb = [int(opz) for opz in linijka.split('x')]
        scianki = [szer*wys,wys*gleb,gleb*szer]
        suma += (2 * sum(scianki) + min(scianki))
    return suma


def wstazki():
    plik = splitLines("Day2_input.txt")
    for linijka in plik:
        szer, wys, gleb = [int(opz) for opz in linijka.split('x')]
        kokarda = [szer * wys * gleb]
        wstazka = [min(szer, wys, gleb)]
        print(kokarda + wstazka)
    return


def main():
    print(ile_kartonow())
    print(wstazki())
if __name__ == '__main__':
    main()