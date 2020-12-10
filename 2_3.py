month = int(input("Введите номер месяца в году: "))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
if month == 1 or month == 2 or month == 12:
    print('list', seasons_list[0])
    print('dict', seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print('list', seasons_list[1])
    print('dict', seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print('list', seasons_list[2])
    print('dict', seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print('list', seasons_list[3])
    print('dict', seasons_dict.get(4))
else:
    print("Не правильно! В году только 12 месяцев.")