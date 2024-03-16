import functions as fc

with open('gielda.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]


def transpozycja(data):
    transposed_data = [list(row) for row in zip(*data)]
    return transposed_data


def wyznaczenie_atrybutu(x: int, data):  # x - indeks argumentu, data - wynik przygotowania danych
    count_data = fc.counting(data)
    attribute_count_values = count_data[x]
    attribute_count_decision_values = fc.counting_decision_attribiute(data[x], data)
    return attribute_count_values, attribute_count_decision_values, x + 1


dane = transpozycja(data)
count_att, decision_att, ind = wyznaczenie_atrybutu(0, dane)

print(f'entropia dla klasy decyzyjnej wynosi: {fc.decision_entropy(dane)}')
print(f'wartosc funkcji informacji wynosi:'
      f' {fc.info(count_att, decision_att)} dla atrybutu nr {ind}')
print(f'wartosc przyrostu informacji wynosi:'
      f' {fc.info_gain(count_att, decision_att, dane)} dla atrybutu nr {ind}')
print(f'zrownowazony przyrost informacji wynosi:'
      f' {fc.balanced_information_growth(count_att, decision_att, dane)} dla atrybutu nr {ind}')
