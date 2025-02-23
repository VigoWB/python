from klasy import Kwadrator

def suma_kwadratora(dane):
    ile_pozycji = len(dane)
    suma = ile_pozycji*ile_pozycji
    #print(ile_pozycji, suma)
    '''for abx in range(0, ile_pozycji):
        for xba in range(0, ile_pozycji):
            suma += (xba+abx)'''
    return suma

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.print()
    kwa.pretty()
    dane = kwa.get()
    print(suma_kwadratora(dane))