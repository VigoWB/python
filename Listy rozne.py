import random
random.seed(0)

def lista(policz):

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

    sumaab: list = zbiora + zbiorb
    iloczynab: list = []#te ktore sa w obu

    for cya in zbiora:
        if cya in zbiorb:
            iloczynab.append(cya)
    for dya in zbiora:
        if dya in iloczynab:
            zbiora.remove(dya)
    print(f"Zbiory: ", sumaab, zbiora, iloczynab)
    return



def merge(lis1: list, lis2: list) -> list:
    lismerg: list = []
    listrange = len(lis1) + len(lis2)
    ptra = 0
    ptrb = 0

    for _ in range(listrange):
        if ptra == len(lis1):
            lismerg.append(lis2[ptrb])
            ptrb += 1
            continue

        if ptrb == len(lis2):
            lismerg.append(lis1[ptra])
            ptra += 1
            continue

        if lis1[ptra] >= lis2[ptrb]:
            lismerg.append(lis2[ptrb])
            ptrb += 1
            continue

        if lis1[ptra] < lis2[ptrb]:
            lismerg.append(lis1[ptra])
            ptra += 1
            continue
    return lismerg



def genlist(rozmiar:int, wmin: int, wmax:int) -> list:
    do_dziel: list = []
    for tro in range(rozmiar):
        do_dziel.append(random.randint(wmin, wmax))
    print(f"Lista do dzielenia: ", do_dziel)
    return do_dziel



def dziel(arg: list)-> list:
    if len(arg) == 2:
        return merge(arg[:1], arg[-1:])
    if len(arg) == 1:
        return merge(arg[:1], [])
    else:
        srodek = len(arg) // 2
        return merge(dziel(arg[0:srodek]), dziel(arg[srodek:len(arg)]))


def main():
    losowalista = genlist(4,1,20)
    print(dziel(losowalista))
    # print(merge())
    # lis1 = [1, 2, 3, 5, 8]
    # lis2 = [2, 4, 6, 8, 10]
    # print(merge(lis1, lis2))
    #generator()
    #zbiory()



if __name__ == '__main__':
    main()