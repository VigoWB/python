# Programowe zadania

---

---

## Adventy

[Advent of Code 2015](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/Advent%20of%20Code%202015%201c4b9c4e1d32809d8b66e3969b56e565.md)

[Advent of Code 2016](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/Advent%20of%20Code%202016%201f9b9c4e1d3280b999b6cd8c86565b65.md)

[Advent of Code 2017](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/Advent%20of%20Code%202017%201f9b9c4e1d328045bbe4f6b51daaa159.md)

## Słowa parzyste i nieparzyste

Napisz funkcje `slowa_parzyste`, które na podstawie argumentu będącego listą napisów zwróci tylko te elementy które mają parzystą ilość znaków.

<aside>
💡 Przykładowo "mama", "kot", "błotko" zwróci "mama" i "błotko"

</aside>

Ważne ma przyjmować listę słów i zwrócić listę słów.

Napisz klon funkcji `slowa_parzyste` który będzie zwracał wyłącznie **słowa o nieparzystej długości**, jednak goblin który pracował nad przygotowaniem danych wejściowych do programu pomieszał napisy z liczbami. Twoim zadniem jest przefiltrować słowa nieparzyste, a elementy nie będące napisem pozostawić bez zmiany:

Dane wejściowe

```jsx
["kot", 2, "buka", 3.0, "goblin", 7, "jemioła"]
```

Oczekiwane wyjście

```jsx
['kot', 2, 3.0, 7, 'jemioła']
```

### Podpowiedź

Do sprawdzania typu danych użyj sytemowej funkcji python’a `type` która poinformuje cię jakiego typu jest dana zmienna:

```python
type("kakałko") 
> str
type(2)
> int
type(3.1)
> float
type(True)
> bool
type([1,2,3])
> list
type((1,2))
> tuple
type({'a': "BBB"})
> dict
type(1 + 1j)
> complex
```

### moje bugi juz dzialaja

```python
def wybieranko(listacala):
    odpowiedzi = []
    for slowo in listacala:
		    if type(slowo) != str:
            odpowiedzi.append(slowo)
            continue
        if len(slowo) % 2 == 1:
            odpowiedzi.append(slowo)     
    return odpowiedzi

if __name__ == '__main__':
    listacala = ["kot", 2, "buka", 3.0, "goblin", 7, "jemioła"]
    listanowa = wybieranko(listacala)
    print(listanowa)
```

### Rozwiązanie

```python
def slowa_nieparzyste(inc):
    otp = []
    for word in inc:
        if type(word) != str:
            otp.append(word)
            continue
        if len(word) % 2 == 1:
            otp.append(word)
    return otp

if __name__ == '__main__':
    print(slowa_nieparzyste(["kot", 2, "buka", 3.0, "goblin", 7, "jemioła"]))
```

## Letnie noce

Napisz dwie funkcje `noc_tropikalna` oraz `noc_normalna` obydwie przyjmują jako **argument** listę pomiarów temperatur w formacie float. Pierwsza z nich `noc_tropikalna` ma zwrócić `True` jeśli wszystkie wartości w tablicy są większe lub równe 20. Druga `noc_normalna` ma zwrócić true, jeśli istnieje chociaż jedna wartośc mniejsza niż 20. W obu jeśli warunek nie jest spełniony zwróć wartość `False` . Funkcje napisz w pliku `zadanie_3.py`

Dane wejściowe

<aside>
💡 `noc_tropikalna` [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8] —> True

</aside>

<aside>
💡 `noc_normalna` [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 19.9, 20.3, 20.8] —> True

</aside>

### Rozwiązanie

```python
def noc_tropikalna(cieple):
    for t in cieple:
        if t < 20:
            return False
    return True
def noc_normalna(zimne):
    for t in zimne:
        if t < 20:
            return True
    return False

if __name__ == '__main__':
    print(noc_tropikalna([23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]))
    print(noc_normalna([23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 19.9, 20.3, 20.8]))
```

### Test jednostkowy

```python
import unittest
from zadanie_3 import noc_normalna, noc_tropikalna

class MyTestCase(unittest.TestCase):
    def test_noc_tropikalna_good_set(self):
        result = noc_tropikalna([22.0, 23.0, 24.0, 25.0, 22.0, 21.0, 20.5])
        self.assertTrue(result)

    def test_noc_tropikalna_bad_set(self):
        result = noc_tropikalna([22.0, 19.0, 24.0, 25.0, 22.0, 21.0, 20.5])
        self.assertTrue(not result)

    def test_noc_tropikalna_edge_set(self):
        result = noc_tropikalna([20.1, 20.0, 20.2])
        self.assertTrue(result)

    def test_noc_normalna_good_set(self):
        result = noc_normalna([21.0, 22.0, 19.0])
        self.assertTrue(result)

    def test_noc_normalna_bad_set(self):
        result = noc_normalna([21.0, 22.0, 32.0])
        self.assertTrue(not result)

    def test_noc_normalna_edge_set(self):
        result = noc_normalna([21.0, 20.0, 32.0])
        self.assertTrue(not result)

if __name__ == '__main__':
    unittest.main()

```

Letnie noce 2

Napisz funkcję która zwróci **krotke (tuple)** zawierającą podstawowe informacje na temat przekazanych pomiarów temperatury. Tuple ten powinien składać się z następujących elementów (min_temp, max_temp, średnia_temp,  czy_tropikalna). Temperatura średnia powinna być napisem i mieć dokładność do dwóch miejsc po przecinku (”23.01”), do sprawdzenia czy noc jest tropikalna wykorzystaj funkcję `noc_tropikalna` . Funkcję nazwij `dane_nocne` i zapisz ja w pliku `zadanie_4.py` .

<aside>
💡

W celu zaimportowania `noc_tropikalna` użyj funkcji import zgodnie z formate: `from nazwa_pliku import nazwa_funkcji`

</aside>

```python
def dane_nocne(dane):

tropiki = [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]
print(dane_nocne(tropiki))

> (20.3, 23.0, '21.58', True)
```

### Rozwiązanie

```python
from zadanie_3 import noc_tropikalna

def dane_nocne(tropiki):
    czy_tropikalna = noc_tropikalna(tropiki)
    min_temp = min(tropiki)
    max_temp = max(tropiki)
    srednia_temp = sum(tropiki) / len(tropiki)
    tupla_temp = (min_temp, max_temp, f"{srednia_temp:.2f}", czy_tropikalna)
    return tupla_temp

if __name__ == '__main__':
    tropiki = [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]
    dane_nocne(tropiki)
    print(dane_nocne(tropiki))
```

### Test jednostkowy

```python
import unittest
from zadanie_4 import dane_nocne

class Zadanie4(unittest.TestCase):
    def test_dane_nocne_good_set(self):
        tropiki = [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]
        rdb = dane_nocne(tropiki)
        self.assertTrue(rdb[0] == 20.3)
        self.assertTrue(rdb[1] == 23.0)
        self.assertTrue(rdb[2] == "21.58")
        self.assertTrue(rdb[3])

    def test_dane_nocne_min_set(self):
        tropiki = [10.0, 11.0, 120.0]
        rdb = dane_nocne(tropiki)
        self.assertTrue(rdb[0] == 10.0)
        self.assertTrue(not rdb[3])

    def test_dane_nocne_max_set(self):
        tropiki = [-10.0, -11.0, -5]
        rdb = dane_nocne(tropiki)
        self.assertTrue(rdb[0] == -11.0)
        self.assertTrue(rdb[1] == -5)
        self.assertTrue(not rdb[3])

if __name__ == '__main__':
    unittest.main()

```

## Pliki - początki

Napisz dwie funkcje, `wczytaj` oraz `policz` ich zadania to:

- `wczytaj` - jej zdaniem jest otwarcie pliku `dane.txt` w trybie `readlines` i wypisanie linia po linii ich zawartości do konsoli
- `policz` - jej zadaniem jest otwarcie pliku `dane.txt` w odpowiednim trybie oraz **zwrócenie** ilości linii zapisanych w pliku

<aside>
💡

Krótki opis obsługi najważniejszych elementów obsługi plików:

[04 - Pliki](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/04%20-%20Pliki%2083e5c1693e9f4400a5d513cb711bdfae.md)

</aside>

<aside>
💡

Dane wsadowe:

[dane.txt](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/dane.txt)

</aside>

> Całość zadania zapisz w folderze `04` w pliku `zadanie_4_1.py` , plik `dane.txt` również zapisz w tym folderze
> 

### Rozwiązanie

```python
def wczytaj():
    plik = open('./dane.txt')
    tekst = plik.readlines()
    for line in tekst:
        print(line)
    plik.close()
    return tekst

def policz():
    plik = open('./dane.txt')
    tekst = plik.readlines()
    llini = len(tekst)
    plik.close()
    return llini

if __name__ == '__main__':
    wczytaj()
    print(policz())
    
    
    3333333333333333333333 STARE 333333333333333333333333333333333
def wczytaj():
    plik = open('./home/vigo/python/04/dane.txt') # nie jest konieczna cala sciezka - python wczytuje pliki w referncji do wykonywanego pliku
    # wiec jesli __main__ jest w 04 to wystarczy dane.txt - cala sciezka nie jest potrzebna
    tekst = plik.readlines()
    for line in tekst:
        print(line)
        f.close() # To powinno byc na koncu przed return - tutaj w petli zamykasz plik po kazdej odczytanej linii - czyli po pierwzej linii teezz
        #a i jeszcze referencja do pliku to plik - wiec powinno byc plik.close() a nie f, f w tym kontekscie jest niezdefiniowane - nie ma go
    return tekst

def policz():
    plik = open('./home/vigo/python/04/dane.txt')
    tekst = plik.readlines()
    llini = len(line) # pod jaka zmienna jest to co wczytales z pliku? line w tym kontekscie nie istnieje sprawdz tekst :)
    # brakuje plik.close()
    return llini

if __name__ == '__main__':
    wczytaj()
    policz() # print(policz()) - chcemy wiedziec ile jest tych linii - tam je tylko zwracasz to tutaj warto je wypisac
```

## Hacker rank

```python
def task_1(n: int):
    if n % 2 == 1:
        print('Weird')
    else:
        if n in range(2, 6):
            print('Not Weird')
            return
        if n in range(6, 21):
            print('Weird')
            return
        print('Not Weird')

def task_2(n: int):
    if n % 2 == 1 or n in range(6, 21):
        print('Weird')
    else:
        print('Not Weird')

def task_3(n: int):
    if not (n % 2 == 1 or n in range(6, 21)):
        print('Not Weird')
    else:
        print('Weird')

def task_4(n: int):
    if not (n % 2 == 1) and not (n in range(6, 21)):
        print('Not Weird')
    else:
        print('Weird')

def task_5(n: int):
    if n % 2 == 0 and not (n in range(6, 21)):
        print('Not Weird')
    else:
        print('Weird')

def helper(idx: int):
    print(f"{idx}", end=' - ')
    task_1(idx)

if __name__ == '__main__':
    task_1(18)
    task_4(24)
    helper(1)

```

## Perrrrrmutacje

## split and joint

```python
def split_and_join(line):
    line = line.split(" ")
    s = "-"
    linia = s.join(line)
    return linia

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
```

## mutacje

```jsx
def mutate_string(string, position, character):
    l = list(string)
    l[int(i)] = c
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

## Hackerank STRINGI

```python
def jakistring(napis: str):
    print(napis)
    print(napis.isalnum())  # True     |   True

    # 123Q
    jestalfa = False
    for znak in napis:
        if znak.isalpha():
            jestalfa = True
            break
    print(jestalfa)

    jestcyfra = False
    for znak in napis:
        if znak.isdigit():
            jestcyfra = True
            break
    print(jestcyfra)

    jestlower = False
    for znak in napis:
        if znak.islower():
            jestlower = True
            break
    print(jestlower)

    jestupper = False
    for znak in napis:
        if znak.isupper():
            jestupper = True
            break
    print(jestupper)
```

```python
def count_substring(string, sub_string):
    szukam = len(sub_string)
    wczym = len(string) - szukam    
    cnt = 0
    for idx in range(wczym + 1):
        test = string[idx: idx + szukam]
        if test == sub_string:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
   
```

LOGO H

```python
grubosc = int(input())
n = "H"
#print(grubosc)
#szczalka1
for idf in range(grubosc):
print((n**idf**2).center(grubosc, ' '))
#2belkigora
for idg in range(grubosc + 1):
print(n.rjust(grubosc, ' '))
#srodek
for idg in range(grubosc - 2):
print((n**grubosc**5).center(grubosc*6))
#2belki dol
#szczalka dolna
```

[BINARNIE TO DECYMBALNIE](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/BINARNIE%20TO%20DECYMBALNIE%20125b9c4e1d328048b8b1f6fe4cfdd7da.md)

## 05 - Pętle rewersi i tablice

# Różne zadania z pętli

Napisz dwie funkcje `suma_listy` która zwróci sumę wszystkich elementów w liście, możesz założyć że lista składa się z elementów będących liczbą całkowita `int` . Oraz drugą `ile_wystapien` która mająć zadany pierwszy argument zliczy jego wystąpienia w liście będącej drugim argumentem. Do obu zadań nie używaj wbudowanych funkcji, zrób to za pomocą elementarnych operacji i pętli.

```python
if __name__ == '__main__':
    print(suma_listy([1, 2, 3, 4]))  # 10
    print(suma_listy([999, 2135, 7845, 11565]))  # 22544
    print(suma_listy([-7, 11, -4, 20]))  # 20
    print(ile_wystapien(3, [1, 2, 3, 3, 3, 4, 3]))  # 4
    print(ile_wystapien(1, [1, 0, 1, 0, 1, 0, 1]))  # 5
    print(ile_wystapien(798, [0, 7, 9, 1, 11, 23, 77]))  # 0
    print(ile_wystapien(666, []))  # 0
```

```python
def suma_listy(lista):
    ile_pozycji = len(lista)
    suma = 0
    #for asd in lista:
     #   suma = asd + suma
    for asd in range(0, ile_pozycji):
        suma = suma + lista[asd]
    return suma

def ile_wystapien(szukane, lista):
    suma = 0
    for asd in lista:
        if asd == szukane:
            suma += 1
    return suma
 
def zakresy_wicia(start, stop, krok):
    kroki = start
    zakresowo = []
    if krok == 0:
        return zakresowo
    if krok > 0:
        while kroki < stop:
            zakresowo.append(kroki)
            kroki += krok
    else:
        while kroki > stop:
            zakresowo.append(kroki)
            kroki += krok
    return zakresowo

def trojki_elementy(lista):
    dl_listy = len(lista)
    indeksy = zakresy_wicia(0, dl_listy, 3)
    elementy = []
    for iop in indeksy:
        elementy.append(lista[iop])
    return elementy
    # z podanej listy zwrocic tylko te elementy ktore sa na indeksach 3n
    # koniecznie uzyj zakresy_wicia
    
def trojki_elementy_reverse(lista):
    dl_listy = len(lista) -1
    indeksy = zakresy_wicia(dl_listy,-1 ,-3)
    elementy = []
    for iop in indeksy:
        elementy.append(lista[iop])
    return elementy
    # z podanej listy zwrocic tylko te elementy ktore sa na indeksach 3n ale od konca
    # koniecznie uzyj zakresy_wicia
    
if __name__ == "__main__":
		print(trojki_elementy(['a','b','c','d','e','f','g'])) # ['a','d','g']
    print(trojki_elementy_reverse(['a', 'b', 'c', 'd', 'e', 'f', 'g']))  # ['g','d','a']
		print(zakresy_wicia(3, 0, -1))
    print(zakresy_wicia(-20, -10, 3))
    print(zakresy_wicia(0, 3, 1))
    print(zakresy_wicia(10, 14, 1))
    print(zakresy_wicia(4, 7, 2))
		print (zakresy_wicia (0,20, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,]))
    print(suma_listy([1, 2, 3, 4]))  # 10
    print(suma_listy([999, 2135, 7845, 11565]))  # 22544
    print(suma_listy([-7, 11, -4, 20]))  # 20
    print(ile_wystapien(3, [1, 2, 3, 3, 3, 4, 3]))  # 4
    print(ile_wystapien(1, [1, 0, 1, 0, 1, 0, 1]))  # 5
    print(ile_wystapien(798, [0, 7, 9, 1, 11, 23, 77]))  # 0
    print(ile_wystapien(666, []))  # 0
```

```python
def trojki_elementy_reverse(lista):
    # z podanej listy zwrocic tylko te elementy ktore sa na indeksach 3n ale od konca
    # koniecznie uzyj zakresy_wicia

if __name__ == '__main__':  
```

 

Rewersi

![Messenger_creation_5887140F-7E13-4733-A824-152173317292.jpeg](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/Messenger_creation_5887140F-7E13-4733-A824-152173317292.jpeg)

z

a) plansza do gry - to juz mamy

b) wprowadzanie ruchow - to bedziesz robic

c) przechowanie stanu gry

d) jak juz mamy stan gry to modyfikujemy b - bo wiemy kto sie rusza i ktore pola sa zajete

e) sprawdzanie czy po ruchu plansza sie zmienia - czy dwa pionki otaczaja kolejne n pionkow innego koloru

f) stan koncowy kiedy gra sie konczy i podliczenie pkt

g) glowna petla ktora wszystko zepnie

```python
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
```

**Tablice rozne opcje**

```python
import random

def danewczyt():
    pliczek = open("dane.txt", "r")
    l = 1
    linijki = []
    for wiersze in pliczek.readlines():
        podzielonelinie = wiersze.strip()
        print(f"Linia nr {l}: {podzielonelinie}")
        linijki.append(podzielonelinie)
        l += 1
    print('')
    pliczek.close()

    return linijki

def zdekoduj_kwadrat(test):
    dane = str.split(test,"|")

    if len(dane) != 2:
        print("Złe dane")
        return None
    wielkosc = int(dane[0])
    if wielkosc < 2:
        print("To nie kwadrat")
        return None

    parametry = dane[1]
    tablica = str.split(parametry, ",")

    for idf, igh in enumerate(tablica):
        tablica[idf] = int(igh)
    #print(tablica)

    if len(tablica) != wielkosc ** 2:
        print('Nie zgadza się ilość elementow')
        return None
    kwadratsprawdzony = []
    '''poczatek = 0
    koniec = wielkosc
    for ijk in range(wielkosc):
        temp = tablica[poczatek:koniec]
        koniec += wielkosc
        kwadrat.append(temp)
        poczatek += wielkosc'''
    for idk in range(wielkosc):
        poczatek = idk * wielkosc
        koniec = (idk + 1) * wielkosc
        temp = tablica[poczatek:koniec]
        kwadratsprawdzony.append(temp)
    return kwadratsprawdzony

def tab():
    #n = input("podaj cyfre:" ) #ilosc wierszy no i kolumn
    #tablica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    saturn = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    '''jupiter = [
        [4, 14, 15, 1],
        [9, 7, 6, 12],
        [5, 11, 10, 8],
        [16, 2, 3, 13]
    ]'''
    '''for idx in range(n):
        wiersz = input().split()
        for i in range(len(wiersz)):
            wiersz[i] = int(wiersz[i])
        tablica.append(wiersz)'''
    return saturn

def suma_wiersz(tablica):
    dlugosctablicy = len(tablica)
    sumy = []
    '''for ind, wart in enumerate (tablica):
        print ('Wiersz', ind+1, 'Wartość', sum(wart))'''
    for w in range(dlugosctablicy):
        #print(f"wiersz",(w+1))
        sumaWiersza = 0
        for k in range(dlugosctablicy):
            #print((w, k),(tablica[w][k]))
            sumaWiersza += tablica[w][k]
        #print(sumaWiersza)
        sumy.append(sumaWiersza)
    return sumy

def suma_kolumn(tablica):
    dlugosctablicy = len(tablica)
    sumy = []
    for w in range(dlugosctablicy):
        #print(f"kolumna", (w + 1))
        sumaKolumny = 0
        for k in range(dlugosctablicy):
            #print((w, k),(tablica[w][k]))
            sumaKolumny += tablica[k][w]
        sumy.append(sumaKolumny)
    return sumy

def przekatne(tablica):
    dlugosctablicy = len(tablica)
    przekatna1 = []
    przekatna2 = []
    for p in range(dlugosctablicy):
        przekatna1.append(tablica[p][p])
        przekatna2.append(tablica[p][dlugosctablicy-p-1])
    suma1przek = sum(przekatna1)
    suma2przek = sum(przekatna2)
    return [suma1przek, suma2przek]

def czyonmagiczny(tablica):
    magicznalista = suma_wiersz(tablica)+suma_kolumn(tablica)+przekatne(tablica)
    start = magicznalista[0]
    for idp in range(len(magicznalista)):
        if magicznalista[idp] != start:
            return False
    return True

def generuj_magiczny():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    while a / b != .5 and (a / b) != 1 and (a / b) != 2 and a > (b + c):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

    kwadratm = [[0 for _ in range(3)] for _ in range(3)]
    kwadratm[0][0] = a - b
    kwadratm[0][1] = a + b - c
    kwadratm[0][2] = a + c
    kwadratm[1][0] = a + b + c
    kwadratm[1][1] = a
    kwadratm[1][2] = a - b - c
    kwadratm[2][0] = a - c
    kwadratm[2][1] = a - b + c
    kwadratm[2][2] = a + b
    return kwadratm

def generuj_magiczne(ile):
    kbx = []
    for idx in range(ile):
        kbx.append(generuj_magiczny())
    return kbx

if __name__ == '__main__':
    linie = danewczyt()
    for linia in linie:
        kwadrat = zdekoduj_kwadrat(linia)
        if kwadrat == None:
            print(kwadrat)
        else:
            print(kwadrat, czyonmagiczny(kwadrat))
    #zdekoduj_kwadrat('2|0,1,1,0')
    #print('Wiersze: ',suma_wiersz(testownik))
    #print('Kolumny: ',suma_kolumn(testownik))
    #print('Przekatne: ',przekatne(testownik))
    #print('Magiczny czy nie: ',czyonmagiczny(testownik))
```

## 06 - Wstep do klas

```python
class Wczytywacz:
    plik = ""

    def __init__(self, nazwapliku):
        self.plik = nazwapliku

    def wczytaj(self):
        pliczek = open(self.plik, "r")
        l = 1
        linijki = []
        for wiersze in pliczek.readlines():
            podzielonelinie = wiersze.strip()
            # print(f"Linia nr {l}: {podzielonelinie}")
            linijki.append(podzielonelinie)
            l += 1
        pliczek.close()

        return linijki

class Kwadrat:
    def __init__(self, rozmiar, elementy):
        self.rozmiar = rozmiar
        self.elementy = elementy

    def print(self):
        for idx in range(self.rozmiar):
            print(self.elementy[idx])

class Samochod:
    # nazwa = 'Bugatti'
    _nachodzie = False

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def odpal(self):
        self._nachodzie = True

    def zgas(self):
        self._nachodzie = False

    def czyOdpalony(self):
        return self._nachodzie

    def status(self):
        if self._nachodzie:
            stan = "odpalony"
        else:
            stan = "zgaszony"
        print(f"Samochod {self.nazwa} jest {stan}")

```

```python
from obiektowe.wczytywacz import Samochod
from obiektowe.wczytywacz import Wczytywacz

if __name__ == '__main__':
    # wczytywacz = Wczytywacz('wczytywacz.py')
    # linie = wczytywacz.wczytaj()
    # print(linie)

    estek = Samochod('Ford Mondeo')
    estek.status()
    estek.nazwa = 'PALIO'
    # estek.odpal()
    estek.status()

    remo = Samochod('Renawlt Megane')
    remo.odpal()
    remo.status()

```

[KWADRATOR](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/KWADRATOR%201a2b9c4e1d3280c9844fc9bd877a68d8.md)

[Słowniki dziwko!](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/S%C5%82owniki%20dziwko!%201b1b9c4e1d32802da79efef66f8795d6.md)

[List Comprehensions](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/List%20Comprehensions%201c2b9c4e1d3280029189f6d7455cf11d.md)

[01 - Typy w Pythonie](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/01%20-%20Typy%20w%20Pythonie%201d7b9c4e1d32806aaa05c0282e87f418.md)

[API - REST - HTTP podstawy](Programowe%20zadania%20e07b59f06a054e2893134a9420b9bb5e/API%20-%20REST%20-%20HTTP%20podstawy%2021cb9c4e1d328093a205ef88d682b395.md)