from Advent_2015.scaffolding.utils import loadFile, loadLines




def licz_znaki():
    co_licze = loadLines("Day1_input.txt")
    zebrane_dane = {}
    for linia in co_licze:
        slowa = linia.split()
        for slowo in slowa:
            for znak in slowo:
                if znak in zebrane_dane:
                    zebrane_dane[znak] += 1
                else:
                    zebrane_dane[znak] = 1
    return zebrane_dane


def kiedy_piwnica():
    importowany = loadFile("Day1_input.txt")
    licznik_pietra = 0
    licznik_zmiany = 0
    for linia in importowany:
        slowa = linia.split()
        for slowo in slowa:
            for znak in slowo:
                if znak == '(' in slowo:
                    licznik_pietra += 1
                    licznik_zmiany += 1
                if znak == ')' in slowo:
                    licznik_pietra -= 1
                    licznik_zmiany += 1
                if licznik_pietra == -1:
                    print("piwnica")
                    break
    return licznik_zmiany

def main():
    #plik = loadLines("Day1_input.txt")
    #print(plik_wczytaj_linie(plik))
    print(licz_znaki())
    print(kiedy_piwnica())

if __name__ == '__main__':
    main()