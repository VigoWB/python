class Instrukcja:
    def __init__(self, linia: str) -> None:
        self.operacje = None
        self.start = (0, 0)
        self.stop = (999, 999)
        self.parse(linia)


    def parse(self, linia: str):

        return None