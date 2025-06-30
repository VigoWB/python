# KWADRATOR

Uruchomienie kwadratora

```python
from kwadrator import Kwadrator

if __name__ == '__main__':
    kwa = Kwadrator()
    kwa.print()
    kwa.pretty()
```

```python
import random

class Kwadrator:
    def __init__(self):
        self.size = random.randint(3, 12)
        self.elements = self.__clear()
        self.__gen()

    def __clear(self):
        return [[0 for _ in range(0, self.size)] for _ in range(0, self.size)]

    def __gen(self):
        for abx in range(0, self.size):
            for bbx in range(0, self.size):
                self.elements[abx][bbx] = random.randint(0, 100)

    def get(self):
        return self.elements

    def print(self):
        for abx in range(0, self.size):
            print(self.elements[abx])

    def pretty(self):
        for abx in range(0, self.size):
            prefix = ' [' if abx == 0 else '  '
            suffix = '] ' if abx == self.size - 1 else ', '
            print(f"{prefix}{self.elements[abx]}{suffix}")

```

```python
def dodaj_kierunki(data):
    size = len(data)
    for x in range(size):
        for y in range(size):
            data[x][y] *= x+y
    return data

def dd_kierunki(data):
    return [[data[x][y] * (x+y) for y in range(len(data))] for x in range(len(data))]

def wojna_kierunkow(data):
    size = len(data)
    sum_odd = 0
    sum_even = 0
    for x in range(size):
        for y in range(size):
            k = x + y
            if k % 2 == 0:
                sum_even += data[x][y]
            else:
                sum_odd += data[x][y]
    return sum_odd - sum_even
```

Kwadrator posiada trzy przydatne funkcje:

- print - printuje wygenerowany losowy kwadrat
- get - zwraca losowy kwadrat jako tablice tablic
- pretty - printuje losowy kwadrat do konsoli w formie do uzycia jako zmienna:

```python
 [[13, 14, 45, 33, 76, 99, 66, 64, 25, 68, 53, 98], 
  [63, 36, 96, 59, 9, 61, 99, 66, 1, 84, 88, 63], 
  [64, 50, 89, 70, 38, 26, 73, 9, 0, 88, 81, 38], 
  [60, 20, 73, 81, 65, 33, 66, 58, 78, 18, 79, 25], 
  [57, 10, 46, 0, 33, 12, 58, 74, 21, 51, 7, 97], 
  [48, 50, 56, 46, 21, 86, 58, 31, 33, 23, 1, 59], 
  [29, 23, 98, 13, 94, 46, 57, 55, 39, 28, 67, 89], 
  [89, 74, 0, 71, 66, 53, 77, 96, 25, 45, 66, 77], 
  [9, 62, 59, 33, 26, 0, 98, 48, 88, 36, 81, 63], 
  [29, 81, 85, 65, 88, 99, 0, 36, 91, 38, 30, 2], 
  [24, 75, 14, 14, 27, 1, 95, 97, 76, 60, 72, 3], 
  [85, 35, 16, 85, 23, 75, 62, 67, 69, 90, 81, 24]] 

Process finished with exit code 0
```

Napisz osobne funkcje które dla losowego kwadratu wylicza:

- sumę wszystkich jego elementów
- sumę parzystych wierszy
- oblicz srednia elementow - suma / ilosc elementow
    - zamien wszystkie elementy w kwadracie ktore sa ≤ sredniej wartoscia `None`
    - pomnoz wszystkie elelementy w kwadracie ktore sa > sredniej razy dwa, te ktore sa ≤ srednia zastap -1
- sume wartosci ktore posiadaja indeksy (x,y) takie ze x+y jest wielokrotnoscia 3
- wypisz transpozycje kwadratu - zamiana wierszy z kolumnami
- obroc kwadrat o 90’ w prawo (pierwszy wiersz staje sie ostatnia kolumna)
- jesli elementy maja ideksy (x,y) wylicz dla kazdego elementu jego “kierunkowy” (x+y)
    - wypisz kwadrat gdzie kazdy element to jego wartosc * kierunkowy
    - oblicz roznice sum elementow o kierunkowym parzystym a kierunkowym nieparzystym

**APPENDY**

- napisz funkcję która pomnoży elementy w liście tyle razy jaka jest ich wartość:
    - dla wsadu [0,1,2] wynikiem bedzie [1,2,2]
    - dla wsadu [2,4] wynikiem będzie [2,2,4,4,4,4]
    - `Lista wsadowa zawsze bedzie posortowana rosnaco, i bedzie zawierac wylacznie liczby calkowite`
    - `Funkcja powinna akceptować listę i zwracać listę`

nie ta strona 😆 

PIT-28 → za okres kiedy byla prowadzona dzialnosc

PIT-37 → 

Wyslac zgloszenie na infolinie - brak informacji dostepu do PIT-37

info.epit@mf.gov.pl

- telefon do kontaktu jako informacja zwrotna w zgloszeniu