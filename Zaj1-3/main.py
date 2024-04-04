import functions as fc

with open('gielda.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]

dane = fc.transpozycja(data)
atrybuty = dane[:len(dane) - 1]
count_att, decision_att, ind = fc.wyznaczenie_atrybutu(0, dane)
# for item in dane:
#     print(dane.index(item))
# print(f'entropia dla klasy decyzyjnej wynosi: {fc.decision_entropy(dane)}')
# print(f'wartosc funkcji informacji wynosi:'
#       f' {fc.info(count_att, decision_att)} dla atrybutu nr {ind}')
# print(f'wartosc przyrostu informacji wynosi:'
#       f' {fc.info_gain(count_att, decision_att, dane)} dla atrybutu nr {ind}')
# print(f'zrownowazony przyrost informacji wynosi:'
#       f' {fc.balanced_information_growth(count_att, decision_att, dane)} dla atrybutu nr {ind}')
# for i in range(0, len(dane) - 1):
#     count_att, decision_att, ind = fc.wyznaczenie_atrybutu(i, dane)
#     print(f'zrownowazony przyrost informacji wynosi:'
#        f' {fc.balanced_information_growth(count_att, decision_att, dane)} dla atrybutu nr {ind}')

# best_gain, index = fc.best_info_gain(dane)
# best_gain_att = dane[index]
# print(f'najlepszy przyrost informacji o wartości {best_gain}, występuje dla atrybutu o indeksie: {index}')




