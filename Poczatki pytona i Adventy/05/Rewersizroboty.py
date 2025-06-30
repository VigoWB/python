import re
def naglowek():
    asd = [str(cyferki) for cyferki in range(1, 9)]
    print(' ', '|'.join(asd))
    dzielna_linia()
    return

def dzielna_linia():
    print(' -+-+-+-+-+-+-+-+-+')
    return

def uzupelnij():
    offset_ascii = 65
    przesuniecie = 8
    for ZNAK in range(offset_ascii, offset_ascii + przesuniecie):
        print(chr(ZNAK),'| '*9, end='\n')
        dzielna_linia()
    return

def ruchy():
    flg = False
    while not flg:
        txa = input ("Podaj ruch dla gracza #####: ")
        if re.search (r'[1-8][A-H]', txa):
            return (txa[0], txa[1])
        else:
            print ('Niepoprawny ruch')
    '''cyfra, litera = input(f"Podaj cyfre: {cyfra}, podaj literę: {litera}").split()
    wspolrzedne = (cyfra +', '+ litera)
    r = re.search(r'[1-8][A-H]', wspolrzedne)
    if r:
        print('Pasi')
    else:
        print('NIE')
    print('Współrzędne: ', wspolrzedne)'''
    return wspolrzedne



if __name__ == '__main__':
    #naglowek()
    #uzupelnij()
    ruchy()