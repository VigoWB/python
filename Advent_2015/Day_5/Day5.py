from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def os():
    plik = splitLines("Day5_input.txt")
    szukane_znaki = ["ab", "cd", "pq", "xy"]#'ab' or 'cd' or 'pq' or 'xy'
    znalezione = False
    for linia in plik:
        for literki in szukane_znaki:
            if not znalezione in szukane_znaki:
                bez_ciagu(linia)
            else:
                znalezione = True
                continue
                #print(f"Nie znaleziono znaczkow: {linia}")
    return

def bez_ciagu(linia):
    print(linia)
    return

def z_ciagiem():

    return


# def po():
#     return


def main():
    print(os())
    print(bez_ciagu())

if __name__ == '__main__':
    main()