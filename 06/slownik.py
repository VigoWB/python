def ile_znakow(napis):
    importowany = napis
    ile_znakow = len(importowany)
    doslowny = {}
    for litery in importowany:
        doslowny[litery] = 1
        #for cyfry in range(ile_znakow):
        if litery==litery in doslowny:
            doslowny[litery] += 1
        else:
            continue
    return doslowny

if __name__ == '__main__':
    napis = "ala ma kota"
    print(ile_znakow(napis))