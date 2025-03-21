from slownik import ile_znakow

#def co_za_plik(dokument):
    #plik = open(dokument)
    #return dokument

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


'''def licz_znaki(dokument):
    tekst = str(przygotowka(dokument))
    znk = ile_znakow(tekst)
    licznik = 0
    for ilosc in znk.values():
        licznik += ilosc
    return licznik'''


def main():
    dokument = "przyklad.txt"
    print(liczenie(dokument))
    return


if __name__ == "__main__":
    main()