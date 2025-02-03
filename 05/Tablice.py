def danewczyt():
    pliczek = open("dane.txt", "r")
    l = 1
    for linia in pliczek.readlines():
        print(f"Linia {l}: {linia}", end="")
        #for tu mam sprawdzic czy to kwadrat?
        l += 1
    pliczek.close()
    print()
    return

def zdekoduj_kwadrat():
    test = "2|0,1,1,0"
    dane = str.split(test,"|")
    if len(dane) != 2:
        print("Złe dane")
        return None
    wielkosc = int(dane[0])
    if wielkosc < 2:
        print("To nie kwadrat")
        return None
    parametry = dane[1]
    tablica = str.split(parametry, ",")
    for idf, igh in enumerate(tablica):
        tablica[idf] = int(igh)
    print(tablica)
    if len(tablica) != wielkosc ** 2:
        print('sikalafon')
    kwadrat = []
    poczatek = 0
    koniec = 0
    for ijk in range(len(tablica)):
        print("ijk", ijk)
        for ilp in range(wielkosc):
            temp = tablica[poczatek:koniec]
            koniec += wielkosc
            kwadrat.append(temp)
        poczatek += wielkosc
    print(kwadrat)

    return

def tab():
    #n = input("podaj cyfre:" ) #ilosc wierszy no i kolumn
    #tablica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    saturn = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    '''jupiter = [
        [4, 14, 15, 1],
        [9, 7, 6, 12],
        [5, 11, 10, 8],
        [16, 2, 3, 13]
    ]'''
    '''for idx in range(n):
        wiersz = input().split()
        for i in range(len(wiersz)):
            wiersz[i] = int(wiersz[i])
        tablica.append(wiersz)'''
    return saturn

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
            #print((w, k),(tablica[w][k]))
            sumaKolumny += tablica[k][w]
        sumy.append(sumaKolumny)
    return sumy

def przekatne(tablica):
    dlugosctablicy = len(tablica)
    przekatna1 = []
    przekatna2 = []
    for p in range(dlugosctablicy):
        przekatna1.append(tablica[p][p])
        przekatna2.append(tablica[p][dlugosctablicy-p-1])
    suma1przek = sum(przekatna1)
    suma2przek = sum(przekatna2)
    return [suma1przek, suma2przek]

def czyonmagiczny():
    magicznalista = suma_wiersz(tab())+suma_kolumn(tab())+przekatne(tab())
    start = magicznalista[0]
    for idp in range(len(magicznalista)):
        if magicznalista[idp] != start:
            return False
    return True

if __name__ == '__main__':
    #print('Wiersze: ',suma_wiersz(tab()))
    #print('Kolumny: ',suma_kolumn(tab()))
    #print('Przekatne: ',przekatne(tab()))
    #print('Magiczny czy nie: ',czyonmagiczny())
    danewczyt()
    zdekoduj_kwadrat()