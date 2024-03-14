import math

# zliczanie wystąpien elementow danego argumentu np dla a1 old = 3, mid = 4, new = 3
def counting(data):
    i = 0
    data_count = {}
    for row in data:
        dict_help = {}
        data_count[i] = dict_help
        for value in row:
            dict_help[value] = 0
        for value in row:
            dict_help[value] += 1
        i += 1
    return data_count

# entropia podajemy wynik counting
def entropy(attribute: dict):
    total = sum(attribute.values())
    entropy_val = 0
    for count in attribute.values():
        probability = count / total
        if probability != 0:
            entropy_val -= probability * math.log2(probability)
    return entropy_val

def decision_entropy(data):
    last_row = counting(data)
    last_row = last_row[len(last_row) - 1]
    return entropy(last_row)

#zliczanie kombinacji elementow atrybutu oraz elementow decyzji np. dla a1 old, down : 3, old, up: 0 (nie istnieje)
#podajemy atrybut (transposed data) oraz wykorzystywane dane
def counting_decision_attribiute(transposed_data, data):
    count_decision_attribiute = {}
    last_row = data[-1]
    for item in transposed_data:
        count_decision_attribiute[f'{item}'] = 0
    for key in count_decision_attribiute:
        j = 0
        i = 0
        help_dict = {}
        for item in last_row:
            if transposed_data[j] == key:
                help_dict[f'{item}'] = 0
            j += 1
        for item in last_row:
            if transposed_data[i] == key:
                help_dict[f'{item}'] += 1
            i += 1
        count_decision_attribiute[key] = help_dict
    return count_decision_attribiute

#liczenie funkcji informacji podajemy wynik counting oraz counting_decision_attribute
def info(attribute, count_decision):
    total = sum(attribute.values())
    info_val = 0
    for key, count in attribute.items():
        probability = count / total
        entropy_val = entropy(count_decision[key])
        info_val += probability * entropy_val
    return info_val

#wyliczanie przyrostu informacji
def info_gain(attribute, count_decision, data):
    last_row = counting(data)
    last_row = last_row[len(last_row) - 1]
    return entropy(last_row) - info(attribute, count_decision)








