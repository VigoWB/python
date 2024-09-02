def wczytaj():
    plik = open('./dane.txt')
    tekst = plik.readlines()
    for line in tekst:
        print(line)
    plik.close()
    return tekst

def policz():
    plik = open('./dane.txt')
    tekst = plik.readlines()
    llini = len(tekst)
    plik.close()
    return llini


if __name__ == '__main__':
    print("1 FUNKCJA")
    wczytaj()
    print("2 FUNKCJA")
    print(policz())