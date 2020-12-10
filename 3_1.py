print('Привет! Я помогу разделить два числа!')
def func_delenie():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        result = a / b
    except ValueError:
        return 'Ошибка введенного значения'
    except ZeroDivisionError:
        return "Неправильный делитель! Вы не можете использовать ноль в качестве разделителя"
    return result

print(round(func_delenie(), 2))