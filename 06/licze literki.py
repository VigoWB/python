
def plik_wczytaj_linie(plik):
    plik = open(plik)
    tekst = plik.readlines()
    plik.close()
    return tekst

def licz_znaki(plik):
    co_licze = plik_wczytaj_linie(plik)
    zebrane_dane = {}
    licznik_slow = 0
    for linia in co_licze:
        slowa = linia.split()
        licznik_slow += len(slowa)
        for slowo in slowa:
            for znak in slowo:
                if znak in zebrane_dane:
                    zebrane_dane[znak] += 1
                else:
                    zebrane_dane[znak] = 1
    return (zebrane_dane, licznik_slow)


def najczesciej_uzywane_literki(plik):
    zbior_literek = licz_znaki(plik)
    same_literki_ze_slownika = zbior_literek[0]
    lista_liter = list(same_literki_ze_slownika.items())
    lista_liter.sort(key=lambda x: x[1], reverse=True)
    najwiecej_literek = dict(lista_liter[:10])
    return najwiecej_literek


def najczesciej_uzywane_literki_duze(plik):
    zbior_literek = licz_znaki(plik)
    same_literki_ze_slownika = zbior_literek[0]
    suma_wartosci = sum(same_literki_ze_slownika.values())
    return suma_wartosci

def main():
    plik = "przyklad.txt"
    #print(licz_znaki(plik))
    print(najczesciej_uzywane_literki(plik))
    print("Suma literek w slowniku: ", najczesciej_uzywane_literki_duze(plik))
    return



if __name__ == "__main__":
    main()