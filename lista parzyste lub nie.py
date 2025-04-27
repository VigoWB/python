import random

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
    print(f"Max to indeks: [{indeks_max}], i ma on wartosc: ",losowe[indeks_max])
    print(f"Długosc listy to: ",len(losowe))

def main():
    generator()

if __name__ == '__main__':
    main()