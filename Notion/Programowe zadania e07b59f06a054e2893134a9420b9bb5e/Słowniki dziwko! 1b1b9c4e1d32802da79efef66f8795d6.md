# Słowniki dziwko!

## Zadanie 1

Napisz funkcje ktora zliczy unikatowe znaki z napisu przekazanego jako argument, funkcja powinna zwracac slownik znakow wraz z liczba wystapien.

**Przykład**

```python
napis = "ala ma kota"
print(ile_znakow(napis))
```

**Odpowiedź**

```python
{'a': 4, 'l': 1, 'm': 1, 'k': 1, 'o': 1, 't': 1}
```

## Zadanie 2

sumy 2 slownikow

czyli jestli masz 'a': 1, 'c': 2 a w drugim 'a': 3, 'b': 1

![](https://scontent-waw2-2.xx.fbcdn.net/v/t39.30808-1/468550952_10161743671927107_6539531447642777292_n.jpg?stp=c25.0.150.150a_dst-jpg_s100x100_tt6&_nc_cat=101&ccb=1-7&_nc_sid=e99d92&_nc_ohc=gBotCLzt5EwQ7kNvgEsnh6F&_nc_oc=AdjOEaR7ChZ4ufDyxjJKbo1cEwD9Qz5z-qFqNsACIQ4MGMqC6AWhRFgVDe7vkJ1dqio&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-waw2-2.xx&_nc_gid=AfG7t4ilFctnK0DOo-6I8VM&oh=00_AYE02DcQNX81dSFBGf3ZZptsjQ94fMnr5ztv7Cz3lFtDFw&oe=67D76493)

to efektem mam byc a: 4, c:2, b:1

![image.png](S%C5%82owniki%20dziwko!%201b1b9c4e1d32802da79efef66f8795d6/image.png)

![image.png](S%C5%82owniki%20dziwko!%201b1b9c4e1d32802da79efef66f8795d6/image%201.png)

```python
def ile_znakow(napis):
    importowany = "".join(napis.split())
    #ile_znakow = len(importowany)
    doslowny = {}
    for litery in importowany:
        #for cyfry in range(ile_znakow):
        if litery==litery in doslowny:
            doslowny[litery] += 1
        else:
            doslowny[litery] = 1
    return doslowny

def sum_dict(d1, d2):
    #print(d1,d2)
    #d2 = {}
    #d1 = {}
    nowy_slowniczek = {}
    nowy_slowniczek.update(d1)
    for klucze, wartosci in nowy_slowniczek.items():
        print(klucze, wartosci)
    if klucz in nowy_slowniczek:
        nowy_slowniczek[klucze] = wartosc + wartosci
    #for klucz, wartosc in d2.items():
    #    print(klucz, wartosc)

    return #d1, d2, nowy_slowniczek

if __name__ == '__main__':
    napis = "ala ma kota"
    #print(ile_znakow(napis))
    d1 = ile_znakow(napis)
    d2 = ile_znakow("JakIS NaPIS Do SUmoWaNIa")
    print(sum_dict(d1, d2))
```

if*_name_*== '*_main_*':
    # start_zakresu = 23
    # koniec_zakresu = 34
    zakres = generuj_zakres(23, 34)
    # zakres = ['23','24','25',....,'33','34']
    # zakres -> dla kazdego elementu wykonac ile_znakow
    # wynik ile_znakow dodac przez sum_dict do jakiegos slownika ktory 
    # bedzie sledzil laczna ilosc znakow do przygotowania

jak to zrobisz za za pomoca ile_nazkow i sum_dict -> pomysl nad druga wersja w ramach jednej metody nie korzystajac z funkjic ile_znakow i sum_dict

## Nie - do - konca - slowniki

Napisz funkcje ktora zamieni dowolna liczbe dziesietna na liczbe w systemie trojkowym

- wsad do funkcji → liczba dziesietna
- wyjscie - napis z reprezentacja liczby w systemie trojkowym

Przyklady

```python
IN: 2 -> OUT: 2
IN: 4 -> OUT: 11
IN: 3 -> OUT: 10
IN: 9 -> OUT: 100
IN: 10 -> OUT: 101
IN: 27 -> OUT: 1000
```

ZAPIS TROJKOWY

```python
liczba = .... 3^3 *(0-2) + 3^2 * (0-2) + 3^1 * (0-2) + 3^0 * (0-2)
```

# Licze duzo, wiec umiem liczyc

Napisz funkcje która jako argument dostanie nazwę pliku tekstowego, jej zadaniem jest policzyc następujące rzeczy z pliku i zwrocic je jako słownik:

- Ilość lini w pliku
- Ilość słów w pliku
- Ilość znaków w pliku

Na nasze potrzeby możemy założyć że słowo to ciąg znaków otoczony spacjami, lub początkiem linii lub jej końcem:

- `Pies` → jedno słowo
- `Duży pies` → dwa słowa

Znaki to ilość liter lub cyferek lub innych znaków nie będących spacją w słowie:

- `Pies2` → 5 znaków
- `ala ma 123 koty` → 4 slowa 12 znakow

Oczekiwany wynik

```python
{
	'plik': 'jakisplik.txt',
	'linie': 28,
	'slowa': 489,
	'znaki': 9823
}
```

Przykladowy plik

```python
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Curabitur ornare felis eget dolor consequat, ac convallis dui hendrerit.
Sed et augue nunc. Praesent vel est placerat, cursus leo ac, interdum urna.
Proin vulputate varius posuere. Nunc non sem sed justo pulvinar tincidunt at quis velit.
Donec suscipit lacus augue, quis euismod purus rutrum non.
Suspendisse tristique dignissim massa, eu scelerisque purus pulvinar id.

Cras orci lorem, maximus vitae interdum eget, varius et arcu.
Donec turpis dui, tincidunt a rhoncus vel, semper at ligula.
Quisque in euismod leo.
Duis leo urna, sollicitudin sed dolor laoreet, lacinia fermentum eros.
Nullam id massa dapibus, dapibus massa sit amet, ornare ipsum.
Nunc a rutrum justo.
Integer arcu est, vulputate quis hendrerit eget, imperdiet quis felis.
Pellentesque ultrices eros vitae enim feugiat, a maximus leo sollicitudin.
Praesent egestas lacus quis commodo elementum.
Maecenas sollicitudin ipsum tortor, quis venenatis mi condimentum ut.
Aliquam sit amet risus ornare, fringilla ligula sed, ornare orci.
Nullam tortor nibh, rutrum in sapien at, commodo facilisis odio.
Integer condimentum, lorem eu bibendum volutpat, turpis nunc tincidunt lectus, vel dapibus elit dui a enim.
Sed tempor ex vel est maximus ultricies.
```

![](https://scontent-waw2-2.xx.fbcdn.net/v/t39.30808-1/468550952_10161743671927107_6539531447642777292_n.jpg?stp=c25.0.150.150a_dst-jpg_s100x100_tt6&_nc_cat=101&ccb=1-7&_nc_sid=e99d92&_nc_ohc=5kRN6OGl-MIQ7kNvgFaTNyX&_nc_oc=Adnu1n1GNW5MALQVg6Yy-9nIpdtgD4CskGitXPoZeHY55T4rqgQP_vL3a0FuAiHVEo0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-waw2-2.xx&_nc_gid=i21gNH3X_fFNIuiU-uttxQ&oh=00_AYFEv-1TIRnclgkU0Oc__UOotwR8owtMZLccb5_97bkBQA&oe=67E1F093)

## PSEUDOKOD

```sql
def policzrzeczy(nazwapliku)
	linie = wczytaj_plik(nazwapliku)
	slownik = {}
	slownik['linie'] = len(linie)
	slownik['slowa'] = 0
	slownik['znaki'] = 0 
	dla kazdej linii:
	   slowa = podziel slowa z lini
	   slowniki[slowa] += len(slowa)
	   dla kazdego slowa:
		   znaki = podziel znaki ze slowa
		   slowniki[znaki] += len(znaki)
 slownik[plik] = nazwapliku
 return slownik
```