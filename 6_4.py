'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} стоит')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость Town car {self.name} составляет {self.speed} км/ч')
        if self.speed > 60:
            print(f'Скорость машины {self.name} превышает 60 км/ч')
        else:
            print(f'Скорость машины {self.name} допустимая для Town car')

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость Work car {self.name} составляет {self.speed} км/ч')
        if self.speed > 40:
            print(f'Скорость машины {self.name} превышает 40 км/ч')
        else:
            print(f'Скорость машины {self.name} допустимая для Work car')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не является полицейской машиной')

ferrari = SportCar(100, 'Красная', 'ferrari', False)
toyota = TownCar(30, 'белая', 'prius', False)
ford = WorkCar(70, 'черная', 'Focus', False)
lada = PoliceCar(110, 'белая',  'Лада Приора', True)

lada.turn_left()
f'Когда {toyota.turn_right()}, при этом {ferrari.stop()}'
f'{lada.go()}  {lada.show_speed()}'
f'{lada.name} цвет {lada.color}'
f'{ferrari.name} полицейская машина? {ferrari.is_police}'
f'{lada.name} полицейская машина? {lada.is_police}'
ferrari.show_speed()
toyota.show_speed()
ford.show_speed()