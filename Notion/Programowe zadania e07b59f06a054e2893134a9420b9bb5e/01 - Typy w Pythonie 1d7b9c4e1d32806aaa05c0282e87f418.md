# 01 - Typy w Pythonie

Od Pythona 3.5 dodano obsługe `typing` czyli podpowiadania Pythonowi jakiego rodzaju jest:

- zmienna
- argument funkcji
- return funkcji

Pomaga to w łatwy i czytelny sposób sprawdzać i weryfikować czy poprawnie obsługujemy się z danymi i wartościami, powoduje to również nowe rodzaje błędów, np. przypisanie wartości typu napis do zmiennej typu integer lub do wartości logicznej.

Typy w Pythonie można podzielić na dwa rodzaje:

- proste typy wynikające z samego jezyka
- typy customowe wynikające z obiektów, które możemy sami tworzyć

W celu używania typingu składnia jest następująca dla zmiennych

```python
# zmienna bez żadnego typu - jej typ wynika z jej wartosci
abx = "Dwa trzy osiem"
# Zmienna typu string - napis
bbx: str = "To jest napis"
# Zmienna typu int - liczba całkowita
cbx: int = 20
# Zmienna float - liczba zmiennoprzecinkowa
dbx: float = 3.14
# Zmienna list - reprezentuje liste
ltx: list = [1,2,3,4,5]
# zmienna dict - reprezentuje slownik
dtx: dict = {}
# zminna tuple - reprezentuje tuple :3
tpx: tuple = (1,2)
```

Typowania mozna tez uzywac podczas obslugi argumentow funkcji, wtedy jesli argument przekazany do funkcji nie bedzie pasowal do typu funkcji, to Python wywola wyjatek

```python
def funkcja(napis: str, ilosc: int):
	for idx in range(ilosc):
		print(napis)
		
abx = "Hello World"
ctx = 20
# Poprawne wywolanie mimo braku typow - python wyciaga je na podstawie wartosci
funkcja(abx, ctx)

bbx: str = "Hakunamatata"
gtx: int = 30
# poprawne wywolanie typy i wartosci pasuja do siebie
funkcja(bbx, gtx)

jtx: str = "Napis napis"
ftx = 2.3
# zle wywolanie powoduje blad
funkcja(jtx, ftx)
# blad wynika z tego ze ftx -> jest typem float a funkcja akceptuje jako argument
# wylacznie liczbe calkowita (int)
```

Typować również można zwrotki z funkcji (return) w taki sam sposob za pomocą składni

```python
def funkcja(arg1: int, arg2: str) -> str
```

Powoduje to dwie rzeczy:

- wynik funkcji odrazu posiada swoj typ - wiec nie mozna go wsadzic do zmiennej o zdefiniowanym innym typie np. str do int
- wewnetrznie funkcja jest sprawdzana czy zwraca poprawny typ, jesli zadeklarowalismy sie ze funkcja bedzie zwracala `str` a zwracamy `int` i Python to wychwyci powoduje to bląd

Specjalny przypadek to funkcje ktore nie zwracaja wartosci

```python
	def funkcja(arg: list) -> None:
```

W tym przypadku bledem bedzie uzycie return z jakakolwiek wartoscia, sam return jest poprawny tak dlugo jak nie zwraca na zewnatrz wartosci:

```python
def zegarek() -> None;
	# tutaj kod funkcji
	
	# poprawne - nic nie zwracamy
	return
	
	# blad - nie mozmy zwracac zadnej wartosci
	return 200
	
```