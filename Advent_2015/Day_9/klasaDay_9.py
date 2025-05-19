class Mapki:
    def __init__(self):
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

    def __repr__(self):
        return f"{self.miasta} {self.polaczenia}"

    # i ma dwie metody
    # 1. ktora zwraca na zewnatrz wszystkie mozliwe kombinacje
    # 2. ktora zwraca ta sama liste miast - wybrana kombinacja


class Kombinator:
    def __init__(self, miasta: list):
        self.bazoweMiasta = miasta

    def kombinacje(self) -> list:
        # tutaj wygeneruj kombinacje za pomoca itertools
        return []

    def pozostale(self, kombinacja: tuple) -> list:
        # tutaj odejmi miasta ktore sa w kombinacji ld tych kotre sa w self.bazoweMiasta
        return []
