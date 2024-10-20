def na_bajty(liczba):
    wynik =""
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba = liczba // 2
    return wynik
def na_dziesiatki(wejscie):
    wejscie = ""
        for wynik in -len(wejscie):
            2**wejscie + wynik
    return wynik
if __name__ == '__main__':
    print(na_bajty(213))
    print(na_dziesiatki(11010101))