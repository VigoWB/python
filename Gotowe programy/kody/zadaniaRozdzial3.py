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

input ('\nKoniec Enter')

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



import random

print ("\tWitaj w grze 'Jaka to liczba'!")
print ("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print ("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.")
print('Masz na to 5 prob.')
# ustaw wartości początkowe
the_number = random.randint (1, 10)
wylosowana = int (input("Ta liczba to: "))
proby = 5
# pętla zgadywania

while wylosowana != the_number:
    if proby <= 1:
        print ('KONIEC!!!\nZa duzo prob. To byla', the_number)
        break
    if wylosowana > the_number:
        print ("Za duża...")
        proby =- 1
    else:
        print ("Za mała...")
        proby -= 1
    print('Zostalo Ci', proby )
    wylosowana = int (input('Wybierz liczbę: '))


print ("Odgadłeś! Ta liczba to", the_number)
print ("Do osiągnięcia sukcesu potrzebowałeś tylko", proby, "prób!\n")

4. Tym razem trudniejsze wyzwanie. Napisz pseudokod do programu, w którym
gracz i komputer zamienią się rolami w grze z odgadywaniem liczby. To znaczy
gracz wybiera losowo liczbę z przedziału od 1 do 100, a komputer ma ją
odgadnąć. Zanim rozpoczniesz tworzenie algorytmu, pomyśl, w jaki sposób
sam byś zgadywał. Jeśli wszystko się uda, spróbuj napisać kod gry.'''


def zgadywanie():
    #  celuj = int(input("Wybierz liczbe z zakresu 1 - 100"))
    print ('Wybierz liczbe z zakresu 1-100.')
    min = 1
    max = 100
    srednia = max / 2

    while True:
        if int(input('Czy wybrana liczba jest mniejsza niz ', srednia)



if __main__ == "__name__"
          print('casd')
        zgadywanie()
