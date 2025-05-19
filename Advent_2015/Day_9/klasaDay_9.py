class Mapki:
    def __init__(self, linia: str):
        self.miasta: dict = {}
        self.polaczenia: dict = {}

    def dodaj(self, nazwa: str) -> int:
        if nazwa not in self.miasta.keys():
            lepszanazwa: int = len(self.miasta)
            self.miasta[nazwa] = lepszanazwa
            return lepszanazwa
        else:
            return self.miasta.get(nazwa)

    def znajdz(self, nazwa: str) -> int:
        if nazwa in self.miasta.keys():
            return self.miasta[nazwa]
        else:
            return -1

    # i ma dwie metody
    # 1. ktora zwraca na zewnatrz wszystkie mozliwe kombinacje
    # 2. ktora zwraca ta sama liste miast - wybrana kombinacja

    # def __repr__(self):
    #     return f'{self.operacja}, {self.argumenty}, {self.wynik}'
