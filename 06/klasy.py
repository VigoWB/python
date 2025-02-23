import random


class Kwadrator:
    def __init__(self):
        self.size = random.randint(3, 4)
        self.elements = self.__clear()
        self.__gen()

    def __clear(self):
        return [[0 for _ in range(0, self.size)] for _ in range(0, self.size)]

    def __gen(self):
        for abx in range(0, self.size):
            for bbx in range(0, self.size):
                self.elements[abx][bbx] = random.randint(0, 100)

    def get(self):
        return self.elements

    def print(self):
        for abx in range(0, self.size):
            print(self.elements[abx])

    def pretty(self):
        for abx in range(0, self.size):
            prefix = ' [' if abx == 0 else '  '
            suffix = '] ' if abx == self.size - 1 else ', '
            print(f"{prefix}{self.elements[abx]}{suffix}")

    '''def suma(self):
        #print(self.elements)
        ile_pozycji = len(self.size)
        suma = 0
        #print(ile_pozycji)
        for abx in range(0, ile_pozycji):
           suma += abx
        print(suma)
        return suma'''