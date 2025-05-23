def ile_znakow(napis):
    importowany = "".join(napis.split())
    #ile_znakow = len(importowany)
    doslowny = {}
    for litery in importowany:
        #for cyfry in range(ile_znakow):
        if litery==litery in doslowny:
            doslowny[litery] += 1
        else:
            doslowny[litery] = 1
    return doslowny


def generuj_zakres(od, do):
    zakres = []
    for cyfra in range(od, do+1):
        zakres.append(str(cyfra))
    return zakres


def sum_dict(d1, d2):
    nowy_slowniczek = {}
    nowy_slowniczek.update(d1)
    for klucz in d2.keys():
        if klucz in nowy_slowniczek:
           nowy_slowniczek[klucz] += d2[klucz]
        else:
            nowy_slowniczek[klucz] = d2[klucz]
    return nowy_slowniczek


def system_trojki(liczba):
    wynikczy = ""
    while liczba > 0:
        wynikczy = str(liczba % 3) + wynikczy
        liczba = liczba // 3
    return wynikczy


def system_dowolny(liczba, potega):
    if potega < 2 or potega > 9:
        return None
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % potega) + wynik
        liczba = liczba // potega
    return wynik


def main():
    napis = "ala ma kota"
    # print(ile_znakow(napis))
    d1 = ile_znakow(napis)
    d2 = ile_znakow("JakIS NaPIS Do SUmoWaNIa")
    #print(sum_dict(d1, d2))
    start_zakresu = 1
    koniec_zakresu = 15
    zakres = generuj_zakres(start_zakresu, koniec_zakresu)
    asd = {}
    for ele in zakres:
        wynik = ile_znakow(ele)
        asd = sum_dict(asd, wynik)
    print(asd)
    print("1000 na trojkowy: ", system_trojki(1000))
    print("1000 na jaki chcesz: ", system_dowolny(1000, 5))



if __name__ == "__main__":
    main()

