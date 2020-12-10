my_list = input("Введите слова через пробел: ")
for i, el in enumerate(range(my_list.count(' ') + 1), 1):
    word = my_list.split()
    if len(str(word)):
        print(f' {i} {word [el] [:10]}')