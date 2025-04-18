from typing import Final

OP_ON: Final[str] = "turn on"
OP_OFF: Final[str] = "turn off"
OP_TOGGLE: Final[str] = "toggle"

class Instrukcja:
    def __init__(self, linia: str) -> None:
        self.operacja = None
        self.start = (0, 0)
        self.stop = (999, 999)
        self.parse(linia)


    def parse(self, linia: str) -> None:
        # Podziel linię na słowa
        # Przykład: "turn on 931,331 through 939,812"
        # -> ['turn', 'on', '931,331', 'through', '939,812']

        czesci = linia.strip().split()

        # Operacja może być jedno- lub dwuwyrazowa ("turn on", "turn off", "toggle")
        if czesci[0] == "toggle":
            self.operacja = "toggle"
            start_str = czesci[1]
            stop_str = czesci[3]
        else:
            # "turn on" lub "turn off"
            self.operacja = f"{czesci[0]} {czesci[1]}"
            start_str = czesci[2]
            stop_str = czesci[4]

        # Parsowanie współrzędnych start i stop
        self.start = tuple(map(int, start_str.split(',')))
        self.stop = tuple(map(int, stop_str.split(',')))

    def __repr__(self):
        return f'{self.operacja}, {self.start}, {self.stop}' #f"Instrukcja (operacja: {self.operacja}, start->{self.start}, stop->{self.stop})"