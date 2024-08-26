def lista(policz):
    #print(f"Lista ma dlugosc:  {len(lista)}")
    nilosc = 0
    pilosc = 0
    for i in policz:
        #print(i, end=": ")
        if i % 2 == 1:
            #print(f"jest nieparzyste")
            nilosc += 1
        else:
            #print("jest parzyste")
            pilosc += 1
    #print(f"Nieparzystych jest:  {(nilosc)}")
    #print(f"Parzystych jest: {(pilosc)}")
    print(f"Nieparzyste: {(nilosc)}, parzyste: {(pilosc)}")

policz = [1, 2, 3]
lista(policz)
