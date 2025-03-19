from slownik import ile_znakow

def importer():
    plik = open('./przyklad.txt')
    tekst = plik.readlines()
    for line in tekst:
       print(line)
    plik.close()
    llini = len(tekst)
    return llini


def licz_slowa():
    plik = open('./przyklad.txt')
    tekst = str(plik.readlines())
    podzial = tekst.split()
    ctn = 0
    for slowo in podzial:
        ctn += 1
    print(ctn)
    return  ctn


def licz_znaki():
    plik = open('./przyklad.txt')
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
    rozwiazanie = {}
    rozwiazanie["Plik"] = "przyklad.txt"
    rozwiazanie["linie"] = importer()
    rozwiazanie["wyrazy"] = licz_slowa()
    rozwiazanie["znaki"] = licz_znaki()
    print(rozwiazanie)
    #print(licz_slowa())
    return


if __name__ == "__main__":
    main()