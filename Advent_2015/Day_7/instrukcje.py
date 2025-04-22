

class Instrukcja:
    def __init__(self, linia: str) -> None:
        self.operacja = None
        self.wartosci = None
        self.stop = (999, 999)
        self.parse(linia)


    def parse(self, linia: str) -> None:
        # Podziel linię na słowa
        # Przykład: "turn on 931,331 through 939,812"
        # -> ['turn', 'on', '931,331', 'through', '939,812']

        czesci = linia.strip().split('->')
        czesci = list(map(str.strip, czesci))

        # Operacja może być jedno- lub dwuwyrazowa ("turn on", "turn off", "toggle")
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

        if "AND" in czesci[0]:
            print(self.wartosci)
            for i in self.wartosci:
                suma =  i[0] & i[2]
            print("TU JES AND", suma, czesci)

        self.wartosci = tuple(map(str, czesci[0].split()))

        # if czesci[0] == isdigit:
        #     print("TU JEST SAnnnnnnnnnnnnnnnnnnnnnnnnnnMA CYFERKA", czesci)
        # if type(czesci[0]) != 'str':
        # if isinstance(czesci[0], 'int'):
        #     print("TU JEST SAnnnnnnnnnnnnnnnnnnnnnnnnnnMA CYFERKA", czesci)
        # if not type(str) in czesci[0]:
        #     print("TU JEST SAnnnnnnnnnnnnnnnnnnnnnnnnnnMA CYFERKA", czesci)
        #     return


    def __repr__(self):
        return f'{self.operacja}, {self.wartosci}, {self.stop}' #f"Instrukcja (operacja: {self.operacja}, start->{self.start}, stop->{self.stop})"