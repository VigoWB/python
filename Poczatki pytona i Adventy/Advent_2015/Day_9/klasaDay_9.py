from itertools import combinations, permutations


class Mapki:
    def __init__(self):
        self.miasta: dict = {}
        self.polaczenia: dict = {}

    def dodaj(self, nazwa: str) -> int:
        if nazwa not in self.miasta.keys():
            lepszanazwa: int = len(self.miasta) + 1
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


class Kombinator:
    def __init__(self, miasta: list):
        self.bazoweMiasta = miasta

    def permutacje(self) -> permutations:
        return permutations(self.bazoweMiasta)

