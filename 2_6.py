tovary = {
    'Название': str,
    'Цена': int,
    'Количество': int,
    'Единица измерения': str,
}

my_list = []
count = 1

while True:
    otvet = input(f'Добавить товар? [д/н] ').lower()

    if otvet == 'н':
        break
    else:
        info = {}

        for name, type in tovary.items():
            user_input = input(f"Заполните поле '{name}' ")
            info[name] = type(user_input)

        my_list.append((count, info))
        count += 1

analytics = {}

for analytics_key in tovary.keys():
    item_list = []

    for product in my_list:
        item_list.append(product[1][analytics_key])

    analytics[analytics_key] = set(item_list)

print(my_list)
print(analytics)