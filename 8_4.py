"""Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет
базовым для классов-наследников. Эти классы — конкретные типы
оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках
реализовать параметры, уникальные для каждого типа оргтехники."""

class OfficeEquipment:

    def __init__(self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            price: float,):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color
        self.price = price

        self.printable = True if self.type in ("принтер", "ксерокс") else False
        self.scannable = True if self.type in ("сканер", "ксерокс") else False

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color}) {self.price}"

class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)

class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('Сканер', *args)

class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('Ксерокс', *args)

if __name__ == '__main__':
    p = Printer("Epson", "XP-400", "белый", 4000)
    print(p)
    s = Scanner("Samsung", "X4220", "черный", 3000)
    print(s)
    x = Xerox("Sony", "W9010", "серый", 7000)
    print(x)