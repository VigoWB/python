def ile_znakow(napis):
    importowany = "".join(napis.split())
    #ile_znakow = len(importowany)
    doslowny = {}
    for litery in importowany:
        #for cyfry in range(ile_znakow):
        if litery==litery in doslowny:
            doslowny[litery] += 1
        else:
            doslowny[litery] = 1
    return doslowny

def sum_dict(d1, d2):
    nowy_slowniczek = {}
    nowy_slowniczek.update(d1)
    for klucz in d2.keys():
        if klucz in nowy_slowniczek:
           nowy_slowniczek[klucz] += d2[klucz]
        else:
            nowy_slowniczek[klucz] = d2[klucz]
    return d1, d2, nowy_slowniczek

if __name__ == '__main__':
    napis = "ala ma kota"
    #print(ile_znakow(napis))
    d1 = ile_znakow(napis)
    d2 = ile_znakow("JakIS NaPIS Do SUmoWaNIa")
    print(sum_dict(d1, d2))