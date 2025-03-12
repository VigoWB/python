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
    #print(d1,d2)
    nowy_slowniczek = {}
    for klucze, wartosci in d1.items():
        print(klucze,wartosci)
        for klucz in d2.keys():
            #print(klucz)
            if klucze==klucz:
                nowy_slowniczek[klucze] += wartosci
            else:
                nowy_slowniczek[klucze] + d2.keys()

    return d1, d2, nowy_slowniczek

if __name__ == '__main__':
    napis = "ala ma kota"
    #print(ile_znakow(napis))
    d1 = ile_znakow(napis)
    d2 = ile_znakow("jakis napis do sumowania")
    print(sum_dict(d1, d2))