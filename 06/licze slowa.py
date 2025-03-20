from slownik import ile_znakow

def co_za_plik(dokument):
    #plik = open(dokument)
    return dokument

def przygotowka(dokument):
    plik = open(dokument)
    tekst = plik.readlines()
    plik.close()
    return tekst


def licz_slowa(dokument):
    tekst = str(przygotowka(dokument))
    podzial = tekst.split()
    ctn = 0
    for slowo in podzial:
        ctn += 1
    return  ctn


def licz_znaki(dokument):
    tekst = str(przygotowka(dokument))
    znk = ile_znakow(tekst)
    licznik = 0
    for ilosc in znk.values():
        licznik += ilosc
    return licznik


def slownik():
    #rozwiazanie = {}
    #rozwiazanie[importer(plik)] = importer(llini)

    return


def main():
    dokument = "przyklad.txt"
    wczytane_linie = przygotowka(dokument)
    rozwiazanie = {}
    rozwiazanie["Plik"] = co_za_plik(dokument)
    rozwiazanie["linie"] = len(wczytane_linie)
    rozwiazanie["slowa"] = licz_slowa(dokument)
    rozwiazanie["znaki"] = licz_znaki(dokument)
    print(rozwiazanie)


    #print(licz_slowa())
    return


if __name__ == "__main__":
    main()