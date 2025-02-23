from klasy import Kwadrator

def suma_kwadratora(dane):
    ile_pozycji = len(dane)
    sumaWiersza = 0
    for w in range(ile_pozycji):
        for k in range(ile_pozycji):
            sumaWiersza += dane[w][k]
    return sumaWiersza

def ile_parzystych(dane):
    ile_pozycji = len(dane)
    suma_parzystych = 0
    for gop in range(ile_pozycji):
        for opi in range(ile_pozycji):
            if gop % 2:
                suma_parzystych += dane[gop][opi]
    return suma_parzystych

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.print()
    kwa.pretty()
    dane = kwa.get()
    print("Suma listy: ",suma_kwadratora(dane))
    print('Suma parzystych wersów: ',ile_parzystych(dane))