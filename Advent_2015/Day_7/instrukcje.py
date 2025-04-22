

class Instrukcja:
    def __init__(self, linia: str) -> None:
        self.operacja = None
        self.wartosc:  list = []
        self.wynik: str = ''
        self.parse(linia)


    def parse(self, linia: str):
        czesci = linia.strip()
        # czesci = list(map(str.strip, czesci))
        if len(czesci) == 5:
            if czesci[1] == "AND":
                self.operacja = 'AND'
                self.wartosc.append(czesci[0])
                self.wartosc.append(czesci[2])
                self.wynik = czesci[-1]

        # if "RSHIFT" in czesci[0]:
        #     print("RS", czesci)
        # x >> y
        # if "LSHIFT" in czesci[0]:
        # x << y
        #     print("LS", czesci)
        # if "NOT" in czesci[0]:
        # ~ x
        #     print(czesci[0], czesci)
        # if "OR" in czesci[0]:
        # x | y
        #     print("OR TU jest", czesci)
        # self.wartosci = tuple(map(str, czesci[0].split()))

        # if czesci[0] == isdigit:
        #     print("TU JEST SAnnnnnnnnnnnnnnnnnnnnnnnnnnMA CYFERKA", czesci)
        # if type(czesci[0]) != 'str':
        # if isinstance(czesci[0], 'int'):
        #     print("TU JEST SAnnnnnnnnnnnnnnnnnnnnnnnnnnMA CYFERKA", czesci)
        # if not type(str) in czesci[0]:
        #     print("TU JEST SAnnnnnnnnnnnnnnnnnnnnnnnnnnMA CYFERKA", czesci)
        #     return


    def __repr__(self):
        return f'{self.operacja}, {self.wartosc}, {self.wynik}' #f"Instrukcja (operacja: {self.operacja}, start->{self.start}, stop->{self.stop})"