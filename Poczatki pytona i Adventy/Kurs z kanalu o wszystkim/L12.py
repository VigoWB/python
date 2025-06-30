x = 12
y = 2

try:
    lista=[3]
    print(lista[0])
    print(x+4)
    print(x/y)
    print("Linijka po")
except (ZeroDivisionError, TypeError):
    print("Wystąpil jakis błąd")
except:
    print("Inny błąd")
finally:
    print("Finally")
print("dalsze")