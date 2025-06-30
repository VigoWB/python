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
    suma = 0
    dlugosctablicy = len(tablica)
    '''for ind, wart in enumerate (tablica):
        print ('Wiersz', ind+1, 'Wartość', sum(wart))'''
    for w in range(dlugosctablicy):
        print(f"pierwszy for",(w))
        for ww in range(dlugosctablicy):
            #print(tablica[w][ww])
            suma = suma + tablica[w][ww]
            print(suma)



    #w1 = sum(tablica[0])
    #w2 = sum(tablica[1])
    #w3 = sum(tablica[2])
    return sumy#w1, w2, w3

def suma_kolumn(tablica):
    k1 = tablica[0][0] + tablica[1][0] + tablica[2][0]


    return k1

def przekatne(tablica):
    p1 = tablica[0][0] + tablica[1][1] + tablica[2][2]


    return p1

if __name__ == '__main__':
    sumy = tab()
    print(sumy)
    print('Wiersze: ',suma_wiersz(sumy))
    print('Kolumny: ',suma_kolumn(sumy))
    print('Przekatne: ',przekatne(sumy))