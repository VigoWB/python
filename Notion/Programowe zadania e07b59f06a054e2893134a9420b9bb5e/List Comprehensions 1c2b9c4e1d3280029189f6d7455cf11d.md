# List Comprehensions

### Przykład

```python
def main():
    people = ['Jack', 'Emily', 'Mario', 'Savannah']

    comp_people = [p for p in people if len(p) < 6]

    for_people = []
    for p in people:
        if len(p) < 6:
            for_people.append(p)

    filter_people = filter(lambda x: len(x) < 6, people)

    print(comp_people, for_people, list(filter_people))

if __name__ == '__main__':
    main()

```

### Zadanie 1

Za pomocą `list comprehension` wygeneruj następujące:

- listę zwierającę elementy od 0 do 30 `[0,1,2,3 ... 29,30]`
- listę zawierającą elementy od 200 do 220
- listę zawierającą wyłącznie wielokrotności 5 od 500 do 575
- listę zawierającą potęgi pierwszych 20 liczb naturalnych `[1,4,9,16 ... ]`
- przefiltruj listę zawierającą potęgi za pomocą comprehension zwróć wyłącznie parzyste potęgi
- wygeneruj listę zawierającą same 1 o rozmiarze 7
- wygeneruj listę list gdzie każda zawiera 3 kolejne potegi dla liczb 2-5 `[[2,4,8],[3,9,27]...`