from math import factorial

def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)

number = int(input('Пожалуйста введите количество вычисленных факториалов: '))
n = int(number)
for el in fact(n):
    print(el)
