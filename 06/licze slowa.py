def importer():
    plik = open('./przyklad.txt')
    tekst = plik.readlines()
    #for line in tekst:
       #print(line)
    plik.close()
    llini = len(tekst)
    return llini, plik


def licz_slowa():
    plik = open('./przyklad.txt')
    tekst = str(plik.readlines())
    podzial = tekst.split()
    ctn = 0
    for slowo in podzial:
        ctn += 1
    print(ctn)
    return podzial, ctn

def slownik():
    #rozwiazanie = {}
    #rozwiazanie[importer(plik)] = importer(llini)

    return

def main():
    #print("Ilość wierszy to: ",importer())
    rozwiazanie = {}
    rozwiazanie["Plik"] = 21
    print(rozwiazanie)
    print(licz_slowa())
    return


if __name__ == "__main__":
    main()