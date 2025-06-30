'''1 zadanie zmienne prawidlowe i nieprawidlowe
konsekwencja, nazwy opisowe, czytelne, nie za dlugie, nie zaczynec od podkreslnika'''

'''zadanie 2
przysmak1 = input('Co byś zjadl? ')
przysmak2 = input('A moze coś do tego? ')
print('Podano',przysmak1, 'oraz', przysmak2,'\n\tSmacznego!')
input("\nAby zakończyć program, naciśnij klawisz Enter.")'''

#zadanie 3 Napisz program Kalkulator napiwku, w którym użytkownik wprowadza sumę ogólną z rachunku wystawionego przez restaurację. Program powinien potem wyświetlić dwie kwoty napiwku — w wysokości 15 i 20 procent
'''rachunek = float(input('Ile wyniosl rachunek? '))
napiwek20 = rachunek * 0.2
napiwek15 = rachunek * 0.15
print('Napiwek 20 % z tej kwoty to', napiwek20, 'zł, a napiwek 15 % to bedzie', napiwek15, 'zł. Pa.')
input("\nEnter to koniec!")'''

#zadanie 4 Napisz program Sprzedawca samochodów, w którym użytkownik wprowadza
#podstawową cenę samochodu. Program powinien dodać szereg dodatkowych
#opłat, takich jak podatek, opłatę rejestracyjną, prowizję przygotowawczą
#dealera, opłatę za dostarczenie. Oblicz podatek i opłatę rejestracyjną jako
#pewien procent ceny podstawowej. Pozostałe opłaty powinny mieć stałe
#wartości. Wyświetl faktyczną cenę samochodu po doliczeniu wszystkich
#dodatków.
car = float(input('Podstawowa cena samochodu: '))
podatek = car * 0.1
rejestracja = car * 0.05
prowizja = 2000
transport = 505
car_koszt = car + podatek + rejestracja + prowizja + transport
print('Pelen koszt zakupu to: ',car_koszt,'a w tym: \n-podatek(10 %):',podatek,'\n-rejestracja(5 %):',rejestracja,'\n-prowizja dilera:',prowizja,'\n-transport:',transport,)

input("\nEnter to koniec!")