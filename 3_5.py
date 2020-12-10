def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел или Q для выхода: ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Сумма введенных чисел составило: {sum_res}')

my_sum()