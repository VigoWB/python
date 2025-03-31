def plik_wczytaj_linie(plik):
    plik = open(plik)
    tekst = plik.readlines()
    plik.close()
    return tekst


def licz_znaki(plik):
    co_licze = plik_wczytaj_linie(plik)
    zebrane_dane = {}

    for linia in co_licze:
        slowa = linia.split()

        for slowo in slowa:
            for znak in slowo:
                if znak in zebrane_dane:
                    zebrane_dane[znak] += 1
                else:
                    zebrane_dane[znak] = 1
    return zebrane_dane


def main():
    plik = "Day1_input.txt"
    #print(plik_wczytaj_linie(plik))
    print(licz_znaki(plik))

if __name__ == '__main__':
    main()