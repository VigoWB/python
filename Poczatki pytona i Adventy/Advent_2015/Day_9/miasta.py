class Miasta:
    def __init__(self):
        self.miasta = {}

    def dodaj(self, nazwa: str) -> int:
        if nazwa not in self.miasta.keys():
            ptr = len(self.miasta)
            self.miasta[nazwa] = ptr
            return ptr
        else:
            return self.miasta.get(nazwa)

    def znajdz(self, nazwa: str) -> int:
        if nazwa in self.miasta.keys():
            return self.miasta[nazwa]
        else:
            return -1
