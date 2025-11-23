import math

class Circle:
    def __init__(self, radius = 0):
        self._radius = radius
    def get_radius(self):
        return self._radius
    def set_radius(self, radius):
        self._radius = radius
    radius = property(get_radius, set_radius)
    @property
    def get_area(self):
        return math.pi * (self._radius ** 2)
    @property
    def get_circumference(self):
        return 2 * math.pi * self._radius


def main():
    circle = Circle(5)
    print(circle.radius)
    circle.radius = 7
    print(circle.radius)

main()