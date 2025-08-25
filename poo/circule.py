import math
class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return math.pi * (self._radius**2)

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value


circle_1 = Circle(2.5)
print(circle_1.area)
circle_1.radius = 10
print(f'Radius of circle {circle_1.radius}')
print(circle_1.area)