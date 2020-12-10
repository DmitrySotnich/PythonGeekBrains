def int_func(word):
    words = []
    for i in range(len(word)):
        words.append(word[i][0:1].title() + word[i][1:])
    return ' '.join(words)

print(int_func(input('Введите слова через пробел, используя маленькие латинские буквы: ').split()))