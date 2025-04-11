from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def szukanie_ciagu():
    plik = splitLines("Day5_input.txt")
    szukane_znaki = ["ab", "cd", "pq", "xy"]#'ab' or 'cd' or 'pq' or 'xy'
    znalezione_bez = []
    znalezione_z = []
    for linia in plik:
        for ciagi in szukane_znaki:
            if not ciagi in linia:
                znalezione_bez += [linia]
            else:
                znalezione_z += [linia]
                continue
                #print(f"    Nie znaleziono znaczkow: {linia}")
    return znalezione_bez, znalezione_z


def bez_ciagu(znalezione_bez):

    return

def z_ciagiem(znalezione_z):

    return


# def po():
#     return


def main():
    print(szukanie_ciagu())
    #print("bezciagowe: ",bez_ciagu(znalezione_bez))
    #print("Z ciagiem: ", z_ciagiem(znalezione_z))

if __name__ == '__main__':
    main()