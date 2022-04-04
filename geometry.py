"""
Описать абстрактный класс Shape - фигура, у которого:

- абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра
- абстрактный метод get_square (не принимает аргументов) для расчета площади

Во всех дочерних классах методы get_perimeter и get_square должны возвращать
результат вычислений.

Описать класс Circle для круга (дочерний класс для Shape), у которого:

- атрибут r - радиус, тип float
- магический метод __init__, который принимает r
- перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
- перегрузить метод get_square (формула площади: pi * r ** 2)

Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:

- атрибут a - первая сторона, тип float
- атрибут b - вторая сторона, тип float
- магический метод __init__, который принимает a и b
- перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
- перегрузить метод get_square (формула площади: a * b)

Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:

- магический метод __init__, который принимает a, вызывает super
"""
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    r: float

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        b = 2 * pi * self.r
        return b

    def get_square(self):
        c = pi * self.r ** 2
        return c


class Rectangle(Shape):
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        p = 2 * (self.a + self.b)
        return p

    def get_square(self):
        s = self.a * self.b
        return s


class Square(Rectangle):
    def __init__(self, a):
        super(Square, self).__init__(a, b=a)