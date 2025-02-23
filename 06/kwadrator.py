from klasy import Kwadrator

def suma_kwadratora(dane):
    ile_pozycji = len(dane)
    #print(ile_pozycji, suma)
    suma = []
    for w in range(ile_pozycji):
        sumaWiersza = 0
        for k in range(ile_pozycji):
            sumaWiersza += dane[w][k]
        suma.append(sumaWiersza)
    dlugosc = len(suma)
    pelna = 0
    for abc in range(dlugosc):
        pelna = pelna + suma[abc]
    return pelna

def ile_parzystych(dane):
    ile_pozycji = len(dane)

    return ile_pozycji//2

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.print()
    kwa.pretty()
    dane = kwa.get()
    print(suma_kwadratora(dane))
    print(ile_parzystych(dane))