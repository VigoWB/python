produkty = []


def dodaj_produkt(nazwa, cena, ilosc):
    produkt = {
        "nazwa": nazwa,
        "cena": cena,
        "ilosc": ilosc
    }
    produkty.append(produkt)
    print(f"Dodano produkt: {nazwa}")


def usun_produkt(nazwa):
    for produkt in produkty:
        if produkt["nazwa"].lower() == nazwa.lower():
            produkty.remove(produkt)
            print(f"Usunięto produkt: {nazwa}")
            return
    print(f"Produkt '{nazwa}' nie znaleziony.")


def wyswietl_produkty():
    if not produkty:
        print("Brak produktów w liście.")
    else:
        for produkt in produkty:
            print(f"Nazwa: {produkt['nazwa']}")
            print(f"Cena: {produkt['cena']}")
            print(f"Ilość: {produkt['ilosc']}\n")

def main():
    while True:
        print("\n1. Dodaj produkt")
        print("2. Usuń produkt")
        print("3. Wyświetl produkty")
        print("4. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę produktu: ")
            cena = float(input("Podaj cenę: "))
            ilosc = int(input("Podaj ilość: "))
            dodaj_produkt(nazwa, cena, ilosc)
        elif wybor == "2":
            nazwa = input("Podaj nazwę produktu do usunięcia: ")
            usun_produkt(nazwa)
        elif wybor == "3":
            wyswietl_produkty()
        elif wybor == "4":
            break
        else:
            print("Nieprawidłowy wybór. Proszę wybrać ponownie.")


if __name__ == "__main__":
    main()