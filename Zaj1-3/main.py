import test as ts

with open('gielda.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]

transposed_data = [list(row) for row in zip(*data)]

count_data = ts.counting(transposed_data)
attribute_count_values = count_data[0] # dla innych atrybutów trzeba zmienić wartosc w count data
attribute_count_decision_values = ts.counting_decision_attribiute(transposed_data[0], transposed_data)
# dla innych atrybutów trzeba zmienić wartosc w transposed_data

print(f'entropia dla klasy decyzyjnej wynosi: {ts.decision_entropy(transposed_data)}')

print(f'wartosc funkcji informacji wynosi:'
      f' {ts.info(attribute_count_values, attribute_count_decision_values)} dla atrybutu nr 1')
print(f'wartosc przyrostu informacji wynosi:'
      f' {ts.info_gain(attribute_count_values, attribute_count_decision_values, transposed_data)} dla atrybutu nr 1')