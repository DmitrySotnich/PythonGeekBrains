rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('data4.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('newdata4.txt', 'w') as my_file2:
    my_file2.writelines(new_file)