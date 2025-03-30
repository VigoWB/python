def przyklady():
    people = ['Jack', 'Emily', 'Mario', 'Savannah']

    comp_people = [p for p in people if len(p) < 6]

    for_people = []
    for p in people:
        if len(p) < 6:
            for_people.append(p)

    filter_people = filter(lambda x: len(x) < 6, people)

    print(comp_people, for_people, list(filter_people))

def main():
    #listę zwierającę elementy od 0 do 30 [0,1,2,3 ... 29,30]
    lista_liczb = [l for l in range(0,31) ]
    print(lista_liczb)
    #- listę zawierającą elementy od 200 do 220
    lista_liczb2 = [l for l in range(200,221)]
    print(lista_liczb2)
    #- listę zawierającą wyłącznie wielokrotności 5 od 500 do 575
    lista_liczb3 = [l for l in range(500, 576) if l % 5 == 0]
    print(lista_liczb3)
    #- listę zawierającą potęgi pierwszych 20 liczb naturalnych `[1,4,9,16 ... ]`
    lista_liczb4 = [l**2 for l in range(21)]
    print(lista_liczb4)
    #- przefiltruj listę zawierającą potęgi za pomocą comprehension zwróć wyłącznie parzyste potęgi
    lista_liczb5 = [l for l in lista_liczb4 if l % 2 == 0]
    print(lista_liczb5)
    #- wygeneruj listę zawierającą same 1 o rozmiarze 7
    lista_liczb6 =[1 for _ in range(7)]
    print(lista_liczb6)
    #- wygeneruj listę list gdzie każda zawiera 3 kolejne potegi dla liczb 2-5 `[[2,4,8],[3,9,27]...`
    lista_liczb7 = [pow(_, 3) for _ in [_ for _ in range(2,6)]]
    print(lista_liczb7)

if __name__ == '__main__':
    main()
