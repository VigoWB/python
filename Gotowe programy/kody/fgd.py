def losowanie():
    print('Rzucam moneta')
    il_losowan = 0
    il_orlow = 0
    # 1 = Orzeł
    # 2 = Reszka

    while il_losowan < 100:
        il_losowan += 1
        orzel_reszka = random.randint(1, 2)
        if orzel_reszka == 1:
            il_orlow += 1

    print('ilosc reszek ', il_losowan - il_orlow)
    print('ilosc orlow ', il_orlow)
input('\nKoniec -> Enter')