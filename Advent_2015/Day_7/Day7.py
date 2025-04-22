from Advent_2015.Day_7.instrukcje import Instrukcja
from Advent_2015.scaffolding.utils import splitLines


def wczytaj():
    linie = splitLines('Day7_input.txt')
    instrukcje: list[Instrukcja] = []
    for linia in linie:
        instrukcje.append(Instrukcja(linia))
    return instrukcje

def main():
    instrukcje = wczytaj()
    # print(smart_fib(50))
    # for i in range(0, 5):
    #     print(f"FIB {i} - {fib(i)}")
    # return


pamiec = [0 for i in range(10_000)]
pamiec[0] = 1
pamiec[1] = 1

def smart_fib(n: int) -> int:
    for idx in range(1, n + 1):
        pamiec[idx] = pamiec[idx-1] + pamiec[idx-2]
    return pamiec[n]

def fib(n):
    print(f"fib({n})")
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    main()