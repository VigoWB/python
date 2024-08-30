def wybieranko(listacala):
    odpowiedzi = []
    for slowo in listacala:
        if type(slowo) != str:
            odpowiedzi.append(slowo)
            continue
        if len(slowo) % 2 == 1:
            odpowiedzi.append(slowo)
    return odpowiedzi

if __name__ == '__main__':
    listacala = ["kot", 2, "buka", 3.0, "goblin", 7, "jemioła"]
    listanowa = wybieranko(listacala)
    print(listanowa)