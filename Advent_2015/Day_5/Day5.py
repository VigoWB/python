from Advent_2015.scaffolding.utils import splitLines

# wczytaj plik, podziel go na linie
# utworz licznik z wartoscia zero
# dla kazdej linii sprawdz czy:
# - jesli not_nice to nastepna linia
# - jesli nice to dodaj jeden do licznika
#zwroc wartosc licznika
def dziel_licz():
    plik = splitLines('Day5_input.txt')
    licznik = 0
    for napis in plik:
        if czesc_dwa(napis):
            licznik += 1
        # if szukanie_ciagu(napis):
        #     if nice(napis):
        #         licznik += 1
    return licznik



def szukanie_ciagu(napis: str) -> bool:
    szukane_znaki = ["ab", "cd", "pq", "xy"]
    for ciagi in szukane_znaki:
        if ciagi in napis:
            return False
    return True

def czesc_dwa(napis: str) -> bool:
    podwojne = False
    for litera in range(len(napis) - 2):     #szukam podwojne znaki ale rozdzielone
        if napis[litera] == napis[litera + 2]:
            podwojne = True

    powtorka = False
    for znak in range(len(napis) - 1):     #podwojne powtorzone gdzies w wierszu
        if napis[znak:znak +2] in napis[:znak]:
            powtorka = True

    wiersz = False
    if podwojne == True and powtorka == True:
        wiersz = True
    return wiersz

#"Napisz funkcje nice() ktora akceptuje jako argument napis(string) i sprawdza czy dany napis zawiera przynajmniej trzy samogloski,
# oraz przynajmniej jedno powtorzenie bezposrednio po sobie tego samego znaku (np. aa),
# jesli oba warunki sa spelnion zwroc True w przeciwnym wypadku zwroc False"
def nice(napis: str) -> bool:
    samogloski = ["a","e","i","o","u"]
    podwojne = False
    licze = 0
    for literka in napis:
        if literka in samogloski:
            licze += 1

    for litera in range(len(napis) - 1):     #szukam podwojne znaki
        if napis[litera] == napis[litera + 1]:
            podwojne = True

    wiersz = False
    if licze >= 3 and podwojne == True:
        wiersz = True
    return wiersz



def main():
    print(dziel_licz())


if __name__ == '__main__':
    main()