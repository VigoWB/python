from Advent_2015.scaffolding.utils import splitLines

def wykonaj():
    tekst = splitLines('Day8_input.txt')
    znaki = 0
    litery = 0
    for linia in tekst:
        znaki += len(linia)
        litery += sum(c.isalpha() for c in linia)
        if '\"' in linia:
            print(f"tu jest slasz ", {linia})
        if '\\' in linia:
            print(f"tu jest 2x slasz'", {linia})
        # if '\x' in linia:
        #     print(f"tu jest \ x", {linia})
    return

def main():
    # print(wczytaj())
    print(wykonaj())

if __name__ == '__main__':
    main()