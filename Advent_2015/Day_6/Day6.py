from Advent_2015.scaffolding.utils import splitLines
from instrukcje import Instrukcja, OP_ON, OP_OFF, OP_TOGGLE


def wer():
    return


def wczytaj_instrukcje() -> list[Instrukcja]:
    linie = splitLines('Day6_input.txt')
    instrukcje: list[Instrukcja] = []
    for linia in linie:
        instrukcje.append(Instrukcja(linia))
    return instrukcje


def wczytaj_instrukcje() -> list[Instrukcja]:
        linie = splitLines('Day6_input.txt')
        instrukcje: list[Instrukcja] = []
        for linia in linie:
            instrukcje.append(Instrukcja(linia))
        return instrukcje


def main():
    # tpx = Instrukcja("toggle 880,25 through 903,973")
    # print(tpx.operacje, tpx.start, tpx.stop)
    # linie = [
    #     "turn on 931,331 through 939,812",
    #     "turn off 756,53 through 923,339",
    #     "toggle 756,965 through 812,992"
    # ]
    # Plansze 1000 x 1000
    # i w zaleznosci od operacji zapalic lampki od start do koniec lub je zgasic lub zmienic ich stan na przeciwny

    print(wczytaj_instrukcje())
    rozmiar = 1000
    tablica = [[False for _ in range(rozmiar)] for _ in range(rozmiar)]
    instrukcje = wczytaj_instrukcje()
    # dla kazdej instrukcji policzyc start -> koniec w X i Y
    # dla kazdego (ix,iy) -> wykonac operacje
    # for ins in instrukcje:
    #     if ins.operacja == OP_ON:
    #         tablica[0][0] = True
    #         # zapalam lampki
    #         pass
    #     if ins.operacja == OP_OFF:
    #         # gazimy lampki
    #         tablica[0][0] = False
    #         pass
    #     if ins.operacja == OP_TOGGLE:
    #         tablica[0][0] = not tablica[0][0]
    #         # zmienamy lampki
    #         pass


if __name__ == '__main__':
    main()