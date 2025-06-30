# BINARNIE TO DECYMBALNIE

![image.png](BINARNIE%20TO%20DECYMBALNIE%20125b9c4e1d328048b8b1f6fe4cfdd7da/image.png)

```python
def na_bajty(liczba):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba = liczba // 2
    return wynik

def na_dziesiatki(bity: str):
    dlugosc = len(bity)
    wynik = 0
    for index in range(0, dlugosc):
        cos = dlugosc - index - 1
        wynik += (2**cos) * int(bity[index])
    return wynik

if __name__ == "__main__":
    print(na_bajty(213))
    print(na_dziesiatki("11010101"))

```