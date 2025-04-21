from Advent_2015.scaffolding.utils import splitLines


def wczytaj():
    plik = splitLines('Day7_input.txt')
    return plik

def fib(n):
    #F(n) = F(n-1) + F(n-2)
    F = (n-1) + (n-2)
    return F

def main():
    #print(wczytaj())
    print(fib(15))
    return



if __name__ == '__main__':
    main()