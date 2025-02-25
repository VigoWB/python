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
        if gop % 2 == 1:
            for opi in range(ile_pozycji):
                suma_parzystych += dane[gop][opi]
    return suma_parzystych

def srednia(dane):
    ile_elementow = len(dane)*len(dane)
    suma = suma_kwadratora(dane)
    wynik = suma//ile_elementow
    return wynik

def zmiany(dane):
    #zamien wszystkie elementy w kwadracie ktore sa ≤ sredniej wartoscia None
    return

def multi_ele(dane):
    #pomnoz wszystkie elelementy w kwadracie ktore sa > sredniej razy dwa,
    #te ktore sa ≤ srednia zastap -1
    return

def sumy_indeksow(dane):
    #sume wartosci ktore posiadaja indeksy (x,y) takie ze x+y jest wielokrotnoscia 3
    return

def transpozycja(dane):
    #wypisz transpozycje kwadratu - zamiana wierszy z kolumnami
    return

def obrot(dane):
    #obroc kwadrat o 90’ w prawo (pierwszy wiersz staje sie ostatnia kolumna)
    dl = len(dane)
    nowa = []
    #print(dl)
    for last in range(-dl):
        for kolumna in range(dl):
            nowa.append[last][kolumna]
    return nowa

def kierunki(dane):
    #-jesli elementy maja ideksy (x,y) wylicz dla kazdego elementu jego “kierunkowy” (x+y)
    #-wypisz kwadrat gdzie kazdy element to jego wartosc * kierunkowy
    #-oblicz roznice sum elementow o kierunkowym parzystym a kierunkowym nieparzystym
    return

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.print()
    kwa.pretty()
    dane = kwa.get()
    print("Suma listy: ",suma_kwadratora(dane))
    print('Suma parzystych wersów: ',ile_parzystych(dane))
    print("Srednia tablicy: ", srednia(dane))
    print("Obrócony kwadrat: ",obrot(dane))