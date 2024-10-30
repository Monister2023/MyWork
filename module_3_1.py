calls = 0
def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    tuple_=[len(string), string.upper(), string.lower()]
    count_calls(1)
    return tuple(tuple_)


def is_contains(string, list_to_search):
    b= []
    count_calls(1)
    for i in list_to_search:
        b.append(i.lower())
    return string.lower() in b


print(string_info('Цивилизация'))
print(string_info('Блогеры'))
print(is_contains('Броллеры', ['Бро', 'БоРоЛ', 'броЛЛЕРЫ']))
print(is_contains('дось', ['лосЬон', 'лОсОсь']))
print(calls)