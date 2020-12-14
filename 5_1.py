name = input('Введите название файла и формат файла: ')
with open(name,'w') as data:
    while True:
        content = input('Введтите данные: ')
        if content == '':
            break
        data.write(content + '\n')
    print(content)