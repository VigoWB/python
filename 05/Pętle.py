def suma_listy(lista):
    ile_pozycji = len(lista)
    suma = 0
    #for asd in lista:
     #   suma = asd + suma
    for asd in range(0, ile_pozycji):
        suma = suma + lista[asd]
    return suma

def ile_wystapien(szukane, lista):
    suma = 0
    for asd in lista:
        if asd == szukane:
            suma += 1
    return suma

def zakresy_wicia(start, stop, krok, lista):
    start = lista[start]
    stop = lista[stop]
    zakresowo = []
    #for idc in lista:
    print(start)
    print(stop)
    #zakresowo.append(idc)
    return zakresowo

if __name__ == "__main__":
    print (zakresy_wicia (0,20, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,]))
    #print(suma_listy([1, 2, 3, 4]))  # 10
    #print(suma_listy([999, 2135, 7845, 11565]))  # 22544
    #print(suma_listy([-7, 11, -4, 20]))  # 20
    #print(ile_wystapien(3, [1, 2, 3, 3, 3, 4, 3]))  # 4
    #print(ile_wystapien(1, [1, 0, 1, 0, 1, 0, 1]))  # 5
    #print(ile_wystapien(798, [0, 7, 9, 1, 11, 23, 77]))  # 0
    #print(ile_wystapien(666, []))  # 0