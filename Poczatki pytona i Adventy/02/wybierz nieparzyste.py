def ktoreSAparzyste(slowa_parzyste):
    odpowiedz = []
    for slowo in slowa_parzyste:
        if len (slowo) % 2 == 0:
            odpowiedz.append (slowo)
    return odpowiedz



if __name__ == '__main__':
    slowa_parzyste = ["mama", "tata", "kot", "sosenkana", "buka"]
    parzyste = ktoreSAparzyste(slowa_parzyste)
    print(parzyste)