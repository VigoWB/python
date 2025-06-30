from Advent_2015.scaffolding.utils import splitLines


def danepodane()-> list[str]:
    surowe_dane = splitLines('Day1_input.txt')
    return surowe_dane

def kalkulacje(surowe_dane: list[str]) -> int:
    # Kierunki: 0 = Północ, 1 = Wschód, 2 = Południe, 3 = Zachód
    direction = 0  # startujemy patrząc na północ
    x, y = 0, 0    # współrzędne startowe
    zbior = set([])
    steps = surowe_dane[0].split(', ')
    for step in steps:
        turn = step[0]
        blocks = int(step[1:])

        if turn == 'L':
            direction = (direction - 1) % 4
        elif turn == 'R':
            direction = (direction + 1) % 4

        if direction == 0:  # Północ
            y += blocks
        elif direction == 1:  # Wschód
            x += blocks
        elif direction == 2:  # Południe
            y -= blocks
        elif direction == 3:  # Zachód
            x -= blocks

        if (x,y) not in zbior:
            zbior.add((x, y))
        # else:
        #     print(f'jakas pozycja: ',x, y)

    # Odległość Manhattan
    return abs(x) + abs(y)


def first_revisited_distance(surowe_dane: list[str]) -> int:
    # Directions: 0=N, 1=E, 2=S, 3=W
    direction = 0
    x, y = 0, 0
    visited = set()
    visited.add((x, y))

    steps = surowe_dane[0].split(', ')

    # Movement deltas for N, E, S, W
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for step in steps:
        turn = step[0]
        blocks = int(step[1:])

        if turn == 'L':
            direction = (direction - 1) % 4
        elif turn == 'R':
            direction = (direction + 1) % 4

        for _ in range(blocks):
            x += dx[direction]
            y += dy[direction]
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    return 0  # If no location is visited twice

# Example usage:
#print(first_revisited_distance("R8, R4, R4, R8"))  # Output: 4



def main():
    # print(type(danepodane()))
    surowe_dane = danepodane()
    odp = kalkulacje(surowe_dane)
    print(f'Wynik z part 1: ', odp)
    print(f'Wynik z part 2: ', first_revisited_distance(surowe_dane))
    pass


if __name__ == '__main__':
    main()