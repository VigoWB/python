'''def ktoreSAparzyste():
    for x in slowa_parzyste:
        if len(slowa_parzyste) % 2 == 0:
            print(len(slowa_parzyste))

ktoreSAparzyste()'''

if __name__ == '__main__':
    slowa_parzyste = ("mama", "tata", "kot", "sosenkana", "buka")
    odpowiedz = []
    for slowo in slowa_parzyste:
        if len(slowo) % 2 == 0:
            odpowiedz.append(slowo)
    print(odpowiedz)