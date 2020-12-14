with open('data2.txt', 'r') as infile:
    words = 0
    characters = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)
        print(f'Строка № {lineno} {line.splitlines()} состоит из {len(wordslist)} слов.')
print(f'В файле всего {lineno} строк, состоящих из {words} слов и {characters} символов.')
