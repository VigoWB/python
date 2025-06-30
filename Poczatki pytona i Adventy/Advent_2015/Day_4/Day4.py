import hashlib


def simpleCoin(secret: str) -> int:
    return hash(secret, '00000')


def hardCoin(secret: str) -> int:
    return hash(secret, '000000')


def hash(secret: str, expected: str) -> int:
    coin = 0
    while not hashlib.md5(str(secret + str(coin)).encode('utf-8')).hexdigest().startswith(expected):
        if coin > 0 and coin % 10_000 == 0:
            print('.', end='')
        if coin % 800_000 == 0:
            print('')
        coin += 1

    print('')
    return coin


def solve(secret: str) -> None:
    print(f"Simple coin mined in {simpleCoin(secret)}")
    print(f"Hard coin mined in {hardCoin(secret)}")


if __name__ == "__main__":
    solve('ckczppom') # <- tutaj wsadz wartosc z advent of code podana jako input
    # yzbqklnj282749
    # yzbqklnj9962624


    # hash = 'yzbqklnj9962624'
    # print(hashlib.md5(str('yzbqklnj282749').encode('utf-8')).hexdigest())


