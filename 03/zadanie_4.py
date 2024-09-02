from zadanie_3 import noc_tropikalna


def dane_nocne(tropiki):
    czy_tropikalna = noc_tropikalna(tropiki)
    min_temp = min(tropiki)
    max_temp = max(tropiki)
    srednia_temp = sum(tropiki) / len(tropiki)
    tupla_temp = (min_temp, max_temp, :{:2.2}.format(str(srednia_temp)), czy_tropikalna)
    return tupla_temp


if __name__ == '__main__':
    tropiki = [23.0, 22.5, 22.0, 22.1, 21.9, 21.8, 20.9, 20.5, 20.3, 20.8]
    dane_nocne(tropiki)
    print(dane_nocne(tropiki))