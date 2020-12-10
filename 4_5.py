from functools import reduce

def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений от 100 до 1000 {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')