import math


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def norm(self):
        return Vector(self.x / self.magnitude(), self.y / self.magnitude())

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def distance(self, other):
        return Vector(self.x - other.x, self.y - other.y).magnitude()
