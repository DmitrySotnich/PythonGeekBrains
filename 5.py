vyruchka = int(input('Введите данные выручки фирмы (в рублях): '))
izderjka = int(input('Введите данные издержек фирмы (в рублях): '))

if vyruchka > izderjka:
    print('Фирма работает с прибылью в', vyruchka / izderjka, 'раза')
    rab = int(input('Введите количество работников фирмы: '))
    print('Прибыль на одного работника фирмы составит:', vyruchka / rab, 'рублей')

if vyruchka < izderjka:
    print('Фирма работает в убыток')

if vyruchka == izderjka:
    print('Фирма работает в ноль')


// Ответ преподавателя
// vir = float(input('Введите сумму выручки: '))
// izd = float(input('Введите сумму издержек: '))
// if vir < izd:
//    print('Финансовый результат: Прибыль в размере: ', izd - vir)
// elif izd == vir:
//    print('Финансовый результат: Нулевой')
// else:
//    prib = vir - izd
//    print('Финансовый результат: прибыль в размере ', prib)
//    print('Рентабельность выручки: ', prib / vir)
//    print('Прибыль фирмы в расчете на одного сотрудника: ', prib / int(input('Введите количество сотрудников: ')))