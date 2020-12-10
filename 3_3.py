def my_func():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        c = int(input('Введите третье число: '))
        result = [a, b, c]
        result.remove(min(a, b, c))
        return sum(result)
    except ValueError:
        return 'Ошибка введенного значения'

print('Ответ:', my_func())