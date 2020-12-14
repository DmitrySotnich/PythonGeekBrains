def summary():
    try:
        name = input('Введите название файла и формат файла: ')
        with open(name, 'w+') as data:
            number = input('Введите цифры через пробел: ')
            data.writelines(line)
            num = number.split()
            print(sum(map(float, num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()