'''Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т'''

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def work_road(self):
        self.weigth = 25
        self.tickness = 5
        work_road = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'Для строительство дороги необходимо {work_road} тон асфальта')

road = Road(9000, 20)
road.work_road()