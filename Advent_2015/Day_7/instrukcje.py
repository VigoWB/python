

class Instrukcja:
    def __init__(self, linia: str):
        self.operacja = None
        self.wartosc: list = []
        self.wynik: str = ''
        self.parse(linia)


    def parse(self, linia: str):
        czesci = linia.split()
        self.wynik = czesci[-1]
        # czesci = list(map(str.strip, czesci))
        if len(czesci) == 5:
            if czesci[1] == "AND":
                self.operacja = 'AND'
                self.wartosc.append(czesci[0])
                self.wartosc.append(czesci[2])

            if czesci[1] == "OR":
                self.operacja = 'OR'
                self.wartosc.append(czesci[0])
                self.wartosc.append(czesci[2])

            if czesci[1] == "RSHIFT":
                self.operacja = 'RSHIFT'
                self.wartosc.append(czesci[0])
                self.wartosc.append(czesci[2])

            if czesci[1] == "LSHIFT":
                self.operacja = 'LSHIFT'
                self.wartosc.append(czesci[0])
                self.wartosc.append(czesci[2])

        if len(czesci) == 4:
            if czesci[0] == "NOT":
                self.operacja = 'NOT'
                self.wartosc.append(czesci[1])

        if len(czesci) == 3:
            if czesci[1] == "->":
                self.operacja = "ASIGN"
                # self.wartosc = czesci[0]
                self.wartosc.append(czesci[0])

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
        return {self.operacja}, {self.wartosc}, {self.wynik}
        #f'OPERACJA: {self.operacja}, WARTOSCI: {self.wartosc}, WYNIK TO: {self.wynik}'