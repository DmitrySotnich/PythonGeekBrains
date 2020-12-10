my_list = [9, 7, 5, 3, 1]
print(my_list)
num = int(input("Введите номер: "))
a = my_list.count(num)
for el in my_list:
    if a > 0:
        i = my_list.index(num)
        my_list.insert(i + a, num)
        break
    else:
        if num > el:
            j = my_list.index(el)
            my_list.insert(j, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)