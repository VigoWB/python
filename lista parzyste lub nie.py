import random
random.seed(1)

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
    print(f"Nieparzyste: {nilosc}, parzyste: {pilosc}")

    policz = [1, 2, 3]
    lista(policz)

def generator():
    losowe: list = []
    for icp in range(5):
        losowe.append(random.uniform(-5,5))

    max_wartosc = max(losowe)
    indeks_max = losowe.index(max_wartosc)

    for indeks in range(len(losowe)):
        print(f"indeks[{indeks}]:" , losowe[indeks])
    print(f"Max to indeks: [{indeks_max}], i ma on wartość: ",losowe[indeks_max])
    print(f"Długość listy to: ",len(losowe))

def zbiory():
    zbiora: list = []
    #lista = [for i in range(random.randint(2, 12))] for i in zbiora]
    for icp in range(5):
        zbiora.append(random.randint(5,15))
    zbiorb: list = []
    for pci in range(5):
        zbiorb.append(random.randint(7,17))

    sumaab: list = [zbiora + zbiorb]
    iloczynab: list = []#te ktore sa w obu
    roznicaab: list = []
    for cya in zbiora:
        for cyb in zbiorb:
            if cya == cyb:
                iloczynab.append(cyb)
    szukane = 0
    for dya in zbiora:
        for szukane in iloczynab:
            if dya == szukane:
                zbiora -= szukane


    print(f"Zbiory: ", sumaab, roznicaab, iloczynab)
    return


def main():
    #generator()
    zbiory()

if __name__ == '__main__':
    main()