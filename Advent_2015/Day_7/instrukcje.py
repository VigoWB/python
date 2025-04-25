

class Instrukcja:
    def __init__(self, linia: str):
        self.operacja = None
        self.argumenty: list = []
        self.wynik: str = ''
        self.parse(linia)


    def parse(self, linia: str):
        czesci = linia.split()
        # czesci = list(map(str.strip, czesci))
        self.wynik = czesci[-1]
        if len(czesci) == 5:
            if czesci[1] == "AND":
                self.operacja = 'AND'
                self.argumenty.append(czesci[0])
                self.argumenty.append(czesci[2])

            if czesci[1] == "OR":
                self.operacja = 'OR'
                self.argumenty.append(czesci[0])
                self.argumenty.append(czesci[2])

            if czesci[1] == "RSHIFT":
                self.operacja = 'RSHIFT'
                self.argumenty.append(czesci[0])
                self.argumenty.append(czesci[2])

            if czesci[1] == "LSHIFT":
                self.operacja = 'LSHIFT'
                self.argumenty.append(czesci[0])
                self.argumenty.append(czesci[2])

        if len(czesci) == 4:
            if czesci[0] == "NOT":
                self.operacja = 'NOT'
                self.argumenty.append(czesci[1])

        if len(czesci) == 3:
            if czesci[1] == "->":
                self.operacja = "ASSIGN"
                self.argumenty.append(int(czesci[0]))

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

    def __repr__(self):
        return f'{self.operacja}, {self.argumenty}, {self.wynik}'
        #f'OPERACJA: {self.operacja}, WARTOSCI: {self.wartosc}, WYNIK TO: {self.wynik}'