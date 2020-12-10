print('Привет! Помогу возвести в степерь число x в y!')

# Первый вариант через **
def my_func(x, y):
    return x ** y

# Второй вариант через цикл while
def my_func(x, y):
    i = 1
    while y > 0:
        i *= x
        y -= 1
    return i

print(my_func(x = int(input('Введите число x = ')), y = abs(int(input('Введите число y = ')))))