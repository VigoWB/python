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
    dl = len(dane)
    sumatrzy = 0
    for tab in range(dl):
        for bat in range(dl):
            if (tab + bat) % 3 == 0:
                sumatrzy += dane[tab][bat]
    return sumatrzy

def transpozycja(dane):
    #wypisz transpozycje kwadratu - zamiana wierszy z kolumnami
    dl = len(dane)
    nowa = [[0 for _ in range(dl)]for _ in range(dl)]
    for last in range(dl):
        for kolumna in range(dl):
            nowa[kolumna][last] = dane[last][kolumna]
    return nowa

def obrot(dane):
    #obroc kwadrat o 90 stopni w prawo (pierwszy wiersz staje sie ostatnia kolumna)
    dl = len(dane)
    nowa = [[0 for _ in range(dl)]for _ in range(dl)]
    for last in range(dl):
        for kolumna in range(dl):
            nowa[kolumna][dl-1-last] = dane[last][kolumna]
    return nowa

def kierunki(dane):
    #-jesli elementy maja ideksy (x,y) wylicz dla kazdego elementu jego “kierunkowy” (x+y)
    #-wypisz kwadrat gdzie kazdy element to jego wartosc * kierunkowy
    #-oblicz roznice sum elementow o kierunkowym parzystym a kierunkowym nieparzystym
    dl = len(dane)
    kierunki = []
    kwadrat = []
    for tab in range(dl):
        for bat in range(dl):
            kierunki.append(tab+bat)
            kwadrat.append((dane[tab][bat])*(tab+bat))
    return kierunki,kwadrat

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.pretty()
    dane = kwa.get()

    print("Suma listy: ",suma_kwadratora(dane))
    print('Suma parzystych wersów: ',ile_parzystych(dane))
    print("Srednia tablicy: ", srednia(dane))
    print("Suma indeksow podzielnych przez 3: ", sumy_indeksow(dane))
    print("Transpozycja tabeli: ")
    kwa.prettyAny(transpozycja(dane))
    print("Obrócony kwadrat: ")
    kwa.prettyAny(obrot(dane))
    print("Kierunki: ", kierunki(dane))

