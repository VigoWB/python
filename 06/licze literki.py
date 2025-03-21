
def imporcik(plik):
    plik = open(plik)
    tekst = plik.readlines()
    plik.close()
    return tekst

def licz_znaki(plik):
    co_licze = imporcik(plik)
    zebrane_dane = {}
    zebrane_dane["slowa"] = 0
    for linia in co_licze:
        slowo = linia.split()
        zebrane_dane["slowa"] += len(slowo)
        for slowo in linia:
            for znaki in slowo:
                if znaki == znaki in zebrane_dane:
                    zebrane_dane[znaki] += 1
                else:
                    zebrane_dane[znaki] = 1
    return zebrane_dane

def main():
    plik = "przyklad.txt"
    print(licz_znaki(plik))
    return


if __name__ == "__main__":
    main()