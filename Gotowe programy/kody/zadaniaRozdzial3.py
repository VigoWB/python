'''zadanie 1 Napisz program, który symuluje ciasteczko z wróżbą. Program powinien
wyświetlić jedną z pięciu niepowtarzalnych przepowiedni, dokonując losowego
wyboru przy każdym uruchomieniu.
import random

print ('Siema losujemy wrożbę, powodzenia!')

wrozba = random.randint (1, 5)

if wrozba == 1:
    print ('Wróżba nr 1')

elif wrozba == 2:
    print ('Wróżba nr 2')

elif wrozba == 3:
    print ('Wróżba nr 3')

elif wrozba == 4:
    print ('Wróżba nr 4')

elif wrozba == 5:
    print ('Wróżba nr 5')

else:
    print ('Koniec to nie wejdzie nigdy')

input ('\nKoniec Enter')'''

# zadanie 2 Napisz program, który „rzuca” 100 razy monetą, a następnie podaje użytkownikowi liczbę orzełków i reszek
import random
print('Rzucam moneta')
def losowanie():
    il_losowan = 0
    il_orlow = 0
    il_reszek = 0

    while il_losowan < 100:
        il_losowan += 1
        orzel_reszka = random.randint(1, 2)
        if orzel_reszka == 1:
            il_orlow += 1
        elif orzel_reszka == 2:
            il_reszek += 1
    print('ilosc reszek ', il_reszek)
    print('ilosc orlow ', il_orlow)

input('\nKoniec -> Enter')
