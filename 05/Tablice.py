def tab():
    #n = int(input()) # ilosc wierszy
    tablica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    '''for idx in range(n):
        wiersz = input().split()
        for i in range(len(wiersz)):
            wiersz[i] = int(wiersz[i])
        tablica.append(wiersz)'''
    return tablica

def suma_wiersz(tablica):
    dlugosctablicy = len(tablica)
    sumy = []
    '''for ind, wart in enumerate (tablica):
        print ('Wiersz', ind+1, 'Wartość', sum(wart))'''
    for w in range(dlugosctablicy):
        #print(f"wiersz",(w+1))
        sumaWiersza = 0
        for k in range(dlugosctablicy):
            #print((w, k),(tablica[w][k]))
            sumaWiersza += tablica[w][k]
        #print(sumaWiersza)
        sumy.append(sumaWiersza)
    return sumy

def suma_kolumn(tablica):
    dlugosctablicy = len(tablica)
    sumy = []
    for w in range(dlugosctablicy):
        #print(f"kolumna", (w + 1))
        sumaKolumny = 0
        for k in range(dlugosctablicy):
            # print((w, k),(tablica[w][k]))
            sumaKolumny += tablica[k][w]
        #print(sumaKolumny)
        sumy.append(sumaKolumny)
    return sumy

def przekatne(tablica):
    dlugosctablicy = len(tablica)
    sumy = []
    for p in range(dlugosctablicy):
        print(p)

    #p1 = tablica[0][0] + tablica[1][1] + tablica[2][2]
    #p2 = tablica[0][2] + tablica[1][1] + tablica[2][0]

    return sumy

if __name__ == '__main__':
    sumy = tab()
    print(sumy)
    print('Wiersze: ',suma_wiersz(sumy))
    print('Kolumny: ',suma_kolumn(sumy))
    print('Przekatne: ',przekatne(sumy))