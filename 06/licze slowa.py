from slownik import ile_znakow


def przygotowka(dokument):
    plik = open(dokument)
    tekst = plik.readlines()
    plik.close()
    return tekst


def liczenie(dokument):
    wczytane_linie = przygotowka(dokument)
    rozwiazanie = {}
    rozwiazanie["Plik"] = dokument
    rozwiazanie["linie"] = len(wczytane_linie)
    rozwiazanie["slowa"] = 0
    rozwiazanie["znaki"] = 0
    for linia in wczytane_linie:
        slowo = linia.split()
        rozwiazanie["slowa"] += len(slowo)
        for znaki in slowo:
            rozwiazanie["znaki"] += len(znaki)
    return  rozwiazanie


def main():
    dokument = "przyklad.txt"
    print(liczenie(dokument))
    return


if __name__ == "__main__":
    main()