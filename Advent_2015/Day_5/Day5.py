from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def szukanie_ciagu():
    plik = splitLines("Day5_input.txt")
    szukane_znaki = ["ab", "cd", "pq", "xy"]#'ab' or 'cd' or 'pq' or 'xy'
    for linia in plik:
        for ciagi in szukane_znaki:
             if ciagi in linia:
                 return False
    return True



def bez_ciagu(znalezione_bez):
    szukamydalej = znalezione_bez
    #aeiou
    #podwojne znaki
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