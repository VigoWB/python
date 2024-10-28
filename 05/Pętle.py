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

def zakresy_wicia(start, stop, krok):
    kroki = start
    zakresowo = []
    if krok == 0:
        return zakresowo
    if krok > 0:
        while kroki <= stop:
            zakresowo.append(kroki)
            kroki += krok
    else:
        while kroki > stop:
            zakresowo.append(kroki)
            kroki += krok
    return zakresowo

def trojki_elementy(lista):
    dl_listy = len(lista)
    indeksy = zakresy_wicia(1, dl_listy, 3)
    elementy = []
    while indeksy in lista:

        elementy.append(indeksy)
    return elementy
    # z podanej listy zwrocic tylko te elementy ktore sa na indeksach 3n
    # koniecznie uzyj zakresy_wicia

def trojki_elementy_reverse(lista):
    # z podanej listy zwrocic tylko te elementy ktore sa na indeksach 3n ale od konca
    # koniecznie uzyj zakresy_wicia
    return

if __name__ == "__main__":
    #print(trojki_elementy(lista))
    #print(zakresy_wicia(0, 10, 3))
    print(trojki_elementy (['a', 'b', 'c', 'd', 'e', 'f', 'g']))  # ['a','d','g']
    #print(trojki_elementy_reverse (['a', 'b', 'c', 'd', 'e', 'f', 'g']))  # ['g','d','a']
    #print(zakresy_wicia(3, 0, -1))
    #print(zakresy_wicia(-20, -10, 3))
    #print(zakresy_wicia(10, 14, 1))
    #print(zakresy_wicia(4, 7, 2))
    #print(zakresy_wicia (0,20, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,]))
    #print(suma_listy([1, 2, 3, 4]))  # 10
    #print(suma_listy([999, 2135, 7845, 11565]))  # 22544
    #print(suma_listy([-7, 11, -4, 20]))  # 20
    #print(ile_wystapien(3, [1, 2, 3, 3, 3, 4, 3]))  # 4
    #print(ile_wystapien(1, [1, 0, 1, 0, 1, 0, 1]))  # 5
    #print(ile_wystapien(798, [0, 7, 9, 1, 11, 23, 77]))  # 0
    #print(ile_wystapien(666, []))  # 0