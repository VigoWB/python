def WitanieWicia():
    for idx in range(1,21):
        if idx % 5 == 0:
            print("Witaj kolego wielkiego wicia")
            continue
        if idx % 2 == 1:
            print("Witaj kolego")
        if idx % 2 == 0:
            print("Witaj kolego wicia")
#WitanieWicia()
def zamowienia():
    for idx in range(1, 33):
        if idx % 9 == 0:
            print("Pijani beda po 9")
            continue
        if idx % 3 == 0:
            print("Schaboszczak dla tych co lubia przez 3")
            continue
        if idx % 2 == 0:
            print("Makaron dla parzystych")
        if idx % 2 == 1:
            print("Pizza dla nieparzystych")
zamowienia()

