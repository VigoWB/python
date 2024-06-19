from random import randint

los = randint(1,10)
odp = -1
i = 0
print("Zgadnij liczbe z przedialu 1-10")

while odp !=los:
    i+=1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Liczba jest mniejsza")
    elif odp < los:
        print("Liczba jest wieksza")
print("Brawo! odgadles za", i, "razem")