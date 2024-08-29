plik = open("testL14.txt", "a")
if plik.writable():
    plik.write(input("Wprowadz tekst: ") + "\n")
plik.close()

plik = open("testL14.txt", "r")

if plik.readable():
    print("Zawartość pliku: ")
   # tekst = plik.readlines()
   # print(tekst)
   # for l in tekst:
    #    print(l)
    for l in plik:
        print(l)