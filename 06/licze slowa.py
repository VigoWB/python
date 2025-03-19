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
    tekst = plik.readlines()
    podzial = "".join(tekst.split())

    return

def slownik():
    #rozwiazanie = {}
    #rozwiazanie[importer(plik)] = importer(llini)

    return

def main():
    #print("Ilość wierszy to: ",importer())
    rozwiazanie = {}
    rozwiazanie["Plik"] = 21
    print(rozwiazanie)
    return


if __name__ == "__main__":
    main()