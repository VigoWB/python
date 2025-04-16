from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

# wczytaj plik, podziel go na linie
# utworz licznik z wartoscia zero
# dla kazdej linii sprawdz czy:
# - jesli not_nice to nastepna linia
# - jesli nice to dodaj jeden do licznika
# zwroc wartosc licznika
def dziel_licz():
    plik = splitLines('Day5_input.txt')
    licznik = 0
    for napis in plik:
        if szukanie_ciagu(napis) == True and nice(napis) == True:
                licznik += 1
    return licznik



def szukanie_ciagu(napis: str) -> bool:
    plik = napis# splitLines("Day5_input.txt")
    szukane_znaki = ["ab", "cd", "pq", "xy"]
    for linia in plik:
        for ciagi in szukane_znaki:
             if ciagi in linia:
                 return False
    return True


#"Napisz funkcje nice() ktora akceptuje jako argument napis(string) i sprawdza czy dany napis zawiera przynajmniej trzy samogloski,
# oraz przynajmniej jedno powtorzenie bezposrednio po sobie tego samego znaku (np. aa),
# jesli oba warunki sa spelnion zwroc True w przeciwnym wypadku zwroc False"
def nice(napis: str) -> bool:
    # aeiou
    samogloski = ["a","e","i","o","u"]
    podwojne = False
    licze = 0
    for linia in napis:
        for literka in linia:
            if literka in samogloski:
                licze += 1

    #podwojne znaki
    for linia in napis:
        for litera in range(len(linia) - 1):
            if napis[litera] == napis[litera + 1]:
                podwojne = True

    wiersz = False
    if podwojne == True and licze >= 3:
        wiersz = True

    return wiersz



def main():
    napis = splitLines('Day5_input.txt')
    #napis = 'fujcauyucsrxxgatisb'
    print(dziel_licz())
    # print("ciagi ", szukanie_ciagu(napis))
    # print("najs: ", nice(napis))


if __name__ == '__main__':
    main()