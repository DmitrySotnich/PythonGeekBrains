print('Привет! Я имею конвертировать секунды в часы и минуты и отоброжать в формате ЧЧ:ММ:СС')
sec = int(input('Ну, что поехали?! Напиши количество секунд: '))

hours = sec // 3600
min = (sec - hours * 3600) // 60
seconds = sec - (hours * 3600 + min * 60)

print(f'Получается: {hours} ч : {min} мин : {seconds} сек')

// Решение от преподавателя
// second_var = int(input('Введите количесвто секунд:\n'))
// print('hh:mm:ss = {:>2}:{:>2}:{:>2}'.format(second_var//3600, (second_var%3600)//60, second_var%60)
