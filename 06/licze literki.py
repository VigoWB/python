
def plik_wczytaj_linie(plik):
    plik = open(plik)
    tekst = plik.readlines()
    plik.close()
    return tekst

def licz_znaki(plik):
    co_licze = plik_wczytaj_linie(plik)
    zebrane_dane = {}
    zebrane_dane["slowa"] = 0
    for linia in co_licze:
        slowa = linia.split()
        zebrane_dane["slowa"] += len(slowa)
        for slowo in slowa:
            for znak in slowo:
                if znak in zebrane_dane:
                    zebrane_dane[znak] += 1
                else:
                    zebrane_dane[znak] = 1
    del zebrane_dane['slowa']
    return zebrane_dane


def najczesciej_uzywane_literki(plik):
    print(licz_znaki(plik))
    return


def najczesciej_uzywane_literki_all(plik):
    print(licz_znaki(plik))
    return

def main():
    plik = "przyklad.txt"
    print(licz_znaki(plik))
    print(najczesciej_uzywane_literki(plik))
    print(najczesciej_uzywane_literki_all(plik))
    return



if __name__ == "__main__":
    main()