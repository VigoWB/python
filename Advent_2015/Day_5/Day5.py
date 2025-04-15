from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def szukanie_ciagu():
    plik = splitLines("Day5_input.txt")
    szukane_znaki = ["ab", "cd", "pq", "xy"]#'ab' or 'cd' or 'pq' or 'xy'
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

    for literka in napis:
        if literka in samogloski:
            licze += 1
    return licze >= 3

    #podwojne znaki
    for litera in range(len(napis) - 1):
        if napis[litera] == napis[litera + 1]:
            podwojne = True
    return podwojne

    wiersz = False
    if podwojne == True and licze >= 3:
        wiersz = True

    return wiersz


def main():
    napis = 'fujcauyucsrxxgatisb'
    #print("ciagi ", szukanie_ciagu())
    print("najs: ",napis, nice(napis))


if __name__ == '__main__':
    main()