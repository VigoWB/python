def ktoresaparzyste(slowa_parzyste):
    odpowiedz = []
    for slowo in slowa_parzyste:
        if len(slowo) % 2 == 0:
            odpowiedz.append(slowo)
    print(odpowiedz)
    #return odpowiedz

if __name__ == '_main_':
    slowa_parzyste = ("mama", "tata", "kot", "sosenkana", "buka")
    parzyste = ktoresaparzyste(slowa_parzyste)
    print(parzyste)
    print("dasda")