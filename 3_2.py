print('Здравствуйте! Заполните, пожалуйста, анкету!')

def my_func(**kwargs):
     return f'Имя: {name}; Фамилия: {surname}; Год рождения: {year}; Город проживания: {city}; E-mail: {email}; Телефон: {phone}'

name = input('Введите Фамилию: ')
surname = input('Введите Имя: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите e-mail: ')
phone = input('Введите телефон: ')

print((my_func(name=name, surname=surname, year=year, city=city, email=email, phone=phone)))
