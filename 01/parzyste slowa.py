def ktoresanparzyste(slowa_parzyste):
    odpowiedz = []
    for slowo in slowa_parzyste:
        if len(slowo) % 2 == 1:
            odpowiedz.append(slowo)
    return odpowiedz

if __name__ == '_main_':
    slowa_parzyste = ("mama", "tata", "kot", "sosenkana", "buka")
    parzyste = ktoresanparzyste(slowa_parzyste)
    print(parzyste)
