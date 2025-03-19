from slownik import ile_znakow

def co_za_plik(dokument):
    #plik = open(dokument)
    return dokument


def licz_linie(dokument):
    plik = open(dokument)
    tekst = plik.readlines()
    plik.close()
    llini = len(tekst)
    return llini


def licz_slowa(dokument):
    plik = open(dokument)
    tekst = str(plik.readlines())
    podzial = tekst.split()
    ctn = 0
    for slowo in podzial:
        ctn += 1
    print(ctn)
    return  ctn


def licz_znaki(dokument):
    plik = open(dokument)
    tekst = str(plik.readlines())
    podzial = tekst.split()
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
    #print("Ilość wierszy to: ",importer())
    dokument = "przyklad.txt"
    rozwiazanie = {}
    rozwiazanie["Plik"] = co_za_plik(dokument)
    rozwiazanie["linie"] = licz_linie(dokument)
    rozwiazanie["slowa"] = licz_slowa(dokument)
    rozwiazanie["znaki"] = licz_znaki(dokument)
    print(rozwiazanie)
    #print(licz_slowa())
    return


if __name__ == "__main__":
    main()