def noc_tropikalna(cieple):
    for t in cieple:
        if t < 20:
            return False
    return True


def noc_normalna(zimne):
    for t in zimne:
        if t < 20:
            return True
    return False


if __name__ == '__main__':
    print(noc_tropikalna([23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]))
    print(noc_normalna([23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 19.9, 20.3, 20.8]))
    # cieple = [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]
    # zimne = [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 19.9, 20.3, 20.8]
    # noc_tropikalna(cieple)
    # noc_normalna(zimne)
