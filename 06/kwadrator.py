from klasy import Kwadrator
import copy

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
    zmiana = copy.deepcopy(dane)
    dl = len(dane)
    sre = srednia(dane)
    for dan in range(dl):
        for ane in range(dl):
            if dane[dan][ane] <= sre:
                zmiana[dan][ane] = None
    return zmiana

def multi_ele(dane):
    #pomnoz wszystkie elelementy w kwadracie ktore sa > sredniej razy dwa,
    #te ktore sa ≤ srednia zastap -1
    multi = copy.deepcopy(dane)
    dl = len(dane)
    sre = srednia(dane)
    for mu in range(dl):
        for lti in range(dl):
            if dane[mu][lti] > sre:
                multi[mu][lti] *= 2
            else:
                multi[mu][lti] = -1
    return multi

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
    parzyste = 0
    nieparzyste = 0
    for tab in range(dl):
        for bat in range(dl):
            kierunki.append(tab+bat)
            kwadrat.append((dane[tab][bat])*(tab+bat))
            if (tab+bat) % 2 == 0:
               parzyste += dane[tab][bat]
            if (tab+bat) %2 != 0:
                nieparzyste += dane[tab][bat]
    roznica = parzyste - nieparzyste
    return kierunki, kwadrat, parzyste, nieparzyste, roznica

def apendy(dane):
    #- napisz funkcję która pomnoży elementy w liście tyle razy jaka jest ich wartość:
    #- dla wsadu [0,1,2] wynikiem bedzie [1,2,2]
    #- dla wsadu [2,4] wynikiem będzie [2,2,4,4,4,4]
    #- Lista wsadowa zawsze bedzie posortowana rosnaco, i bedzie zawierac wylacznie liczby calkowite
    #- Funkcja powinna akceptować listę i zwracać listę
    do_zmiany = dane
    ile_ma = len(do_zmiany)
    zmieniona = []
    for apo in range(ile_ma):
        for ned in range(apo):
            zmieniona.append(do_zmiany[apo])
    return zmieniona

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.pretty()
    dane = kwa.get()

    '''print("Suma listy: ",suma_kwadratora(dane))
    print('Suma parzystych wersów: ',ile_parzystych(dane))
    print("Srednia tablicy: ", srednia(dane))
    print("Zmiany na None: ", zmiany(dane))
    print("Multi: ", multi_ele(dane))
    print("Suma indeksow podzielnych przez 3: ", sumy_indeksow(dane))
    print("Transpozycja tabeli: ")
    kwa.prettyAny(transpozycja(dane))
    print("Obrócony kwadrat: ")
    kwa.prettyAny(obrot(dane))
    zwrot = kierunki(dane)
    print(f"Kierunki: {zwrot[0]}\nwartosc * kierunek: {zwrot[1]}\nsuma parzystych: {zwrot[2]}"
          f"\nsuma nieparzystych: {zwrot[3]}\nróżnica: {zwrot[4]}")'''
    print(f"Apendy: ", apendy(dane))
