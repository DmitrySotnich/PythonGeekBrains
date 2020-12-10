from sys import argv

name, time, rate, bonus = argv

print('Имя скрипта:', str(name))
print('Количество выработки (часов):', int(time))
print('Cтавка за 1 час работы (рублей): ', int(rate))
print('Премия (рублей): ', int(bonus))
pay = int(time) * int(rate) + int(bonus)
print(f'Заработная плата сотрудника составляет: {pay} рублей')
