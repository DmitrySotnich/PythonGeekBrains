num = int(input('Введите целое положительное число '))

numMax = num % 10
num = num // 10

while num > 10:
    if num % 10 > numMax:
        numMax = num % 10
    num = num // 10

print('Самая большая цифра в числе является', numMax)