from Advent_2015.scaffolding.utils import loadFile, loadLines, splitLines

def os():
    plik = splitLines("Day5_input.txt")
    szukane_znaki = ["ab", "cd", "pq", "xy"]#'ab' or 'cd' or 'pq' or 'xy'
    znalezione = False
    for linia in plik:
        for literki in szukane_znaki:
            if literki in linia:
                znalezione = True
                continue
        if not znalezione:
            print(linia)
                #print(f"Nie znaleziono znaczkow: {linia}")
                #jak to wyswietlic raz?
    return


# def po():
#     return





def main():
    print(os())


if __name__ == '__main__':
    main()