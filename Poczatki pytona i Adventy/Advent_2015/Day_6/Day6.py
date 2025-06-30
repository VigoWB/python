from Advent_2015.scaffolding.utils import splitLines
from instrukcje import Instrukcja, OP_ON, OP_OFF, OP_TOGGLE

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

    #print(wczytaj_instrukcje())
    rozmiar = 1000
    tablica = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)]
    instrukcje = wczytaj_instrukcje()
    # dla kazdej instrukcji policzyc start -> koniec w X i Y
    # dla kazdego (ix,iy) -> wykonac operacje
    for ins in instrukcje:
        for linia in range(ins.start[0], ins.stop[0] + 1):
            for kolumna in range(ins.start[1], ins.stop[1] + 1):
                if ins.operacja == OP_ON:# zapalam lampki
                    tablica[linia][kolumna] += 1
                if ins.operacja == OP_OFF:  # gazimy lampki
                    tablica[linia][kolumna] = max(tablica[linia][kolumna] - 1, 0)
                if ins.operacja == OP_TOGGLE: # zmienamy lampki
                    tablica[linia][kolumna] += 2

    #licze_tru = 150
    # for lic in range(rozmiar):
    #     for nik in range(rozmiar):
    #         if tablica[lic][nik] == type(bool):
    #             continue
    #         else:
    #             licze_tru += tablica[lic][nik]
    print(sum(sum(wiersz) for wiersz in tablica))



if __name__ == '__main__':
    main()