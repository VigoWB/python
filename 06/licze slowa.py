def importer():
    plik = open('./przyklad.txt')
    tekst = plik.readlines()
    #for line in tekst:
       #print(line)
    plik.close()
    llini = len(tekst)
    return llini


def main():
    print(importer())
    return


if __name__ == "__main__":
    main()