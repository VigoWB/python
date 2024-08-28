'''def ktoreSAparzyste():
    for x in slowa_parzyste:
        if len(slowa_parzyste) % 2 == 0:
            print(len(slowa_parzyste))

ktoreSAparzyste()'''

if __name__ == '__main__':
    slowa_parzyste = ("mama", "tata", "kot", "sosenkana", "buka")
    lista = len(slowa_parzyste)
    print(slowa_parzyste)
    print(slowa_parzyste[3])
    odpowiedz = []
    for x in range(0, lista):
        if x % 2 == 0:
            odpowiedz.append(x)
            print(odpowiedz)