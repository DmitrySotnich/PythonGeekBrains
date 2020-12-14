from json import dumps

if __name__ == "__main__":
    results = [{}, {}]

    try:
        with open('data7.txt', encoding='utf-8') as data:
            lines = data.readlines()

        for line in lines:
            name, _, proceeds, expenses = line.split()
            results[0][name] = int(proceeds) - int(expenses)

        results[1]['Srednya pribyl'] = round(
            sum(
                profit for _, profit in results[0].items() if profit > 0
            ) / len(results[0])
        )

        with open('data7.json', "w", encoding='utf-8') as res:
            res.write(dumps(results))
    except IOError as e:
        print(e)
    except ValueError:
        print("Неконсистентные данные")