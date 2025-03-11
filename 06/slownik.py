def ile_znakow(napis):
    importowany = napis
    ile_ma = len(importowany)
    doslowny = {}
    for litery in importowany:
        doslowny[litery]=litery
    print(doslowny)
    return

if __name__ == '__main__':
    napis = "ala ma kota"
    print(ile_znakow(napis))