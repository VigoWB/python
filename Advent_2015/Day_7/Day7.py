from Advent_2015.Day_7.instrukcje import Instrukcja
from Advent_2015.scaffolding.utils import splitLines


def wczytaj()-> list[Instrukcja]:
    # linie = splitLines('test.txt')
    linie = splitLines('Day7_input.txt')
    instrukcje: list[Instrukcja] = []
    for linia in linie:
        instrukcje.append(Instrukcja(linia))
    return instrukcje


def slownik(instrukcje):
    lista_znaczkow: dict = {}
    for ins in instrukcje:
        lista_znaczkow[ins.wynik] = ins
    return lista_znaczkow

def wykonaj(ins: Instrukcja, data: dict) -> int:
    print(ins)
    if ins.operacja == 'ASSIGN':
        if type(ins.argumenty[0]) == int:
            return ins.argumenty[0]
        else:
            return wykonaj(data[ins.argumenty[0]], data)

    print(f"Rozwazam {ins.wynik}")
    argumenty = {}
    for arg in ins.argumenty:
        if type(arg) == str:
            argumenty[arg] = wykonaj(data[arg], data)
        else:
            argumenty[arg] = arg

    if ins.operacja == 'OR':
        return argumenty[ins.argumenty[0]] | argumenty[ins.argumenty[1]]

    if ins.operacja == 'AND':
        return argumenty[ins.argumenty[0]] & argumenty[ins.argumenty[1]]

    if ins.operacja == 'RSHIFT':
        return argumenty[ins.argumenty[0]] >> argumenty[ins.argumenty[1]]

    if ins.operacja == 'LSHIFT':
        return argumenty[ins.argumenty[0]] << argumenty[ins.argumenty[1]]

    if ins.operacja == 'NOT':
        return ~argumenty[ins.argumenty[0]]


    return 1
    # x & y




#sprawdzasz jakie sa argumenty i jaka operacja zaciagnac wartosci wiec abx = wykonaj(TUTAJ OPERACJA DLA B)
# bbx = wykonaj(TUTAJ OPERACJA DLA C)
# return abx [TUTAJ TE BITOWE] bbx
# b OR x -> a
# z OR y -> b
# b OR 4 -> x
# y -> 8
# z -> 16
# takie cos prostego wynik to wedle mojej logiki powinno byc
# x = 12
# b = 24
# a = 26
# kindla nie podlaczylem do ladowania




def main():
    # ins = Instrukcja('af AND ah -> ai')
    # print(ins.wynik, ins)
    instrukcje = wczytaj()
    slownik_operacji = slownik(instrukcje)
    pierwsza_operacja = slownik_operacji["a"]

    wynik = (wykonaj(pierwsza_operacja, slownik_operacji))
    print(wynik)

    # print(smart_fib(50))
    # for i in range(0, 5):
    #     print(f"FIB {i} - {fib(i)}")



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