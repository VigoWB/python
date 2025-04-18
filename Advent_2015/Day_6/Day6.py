#from Advent_2015.scaffolding.utils import splitLines
from instrukcje import Instrukcja


def wer():


    return


def qwe():

    return



def main():
    #tpx = Instrukcja("toggle 880,25 through 903,973")
    #print(tpx.operacje, tpx.start, tpx.stop)
    linie = [
        "turn on 931,331 through 939,812",
        "turn off 756,53 through 923,339",
        "toggle 756,965 through 812,992"
    ]

    for linia in linie:
        instr = Instrukcja(linia)
        print(instr)


if __name__ == '__main__':
    main()