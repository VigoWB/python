def wybieranko(listacala):
    odpowiedzi = []
    for slowo in listacala:
        if len(slowo) % 2 == 1:
            odpowiedzi.append(slowo)
        if type(slowo) != str:
            odpowiedzi.append(slowo)
    return odpowiedzi

if __name__ == '_main_':
    listacala = ["kot", 2, "buka", 3.0, "goblin", 7, "jemioła"]
    listanowa = wybieranko(listacala)
    print(listanowa)
print("towidac")