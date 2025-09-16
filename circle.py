class Circle:
    def __init__(self):
        self.diameter = 0
        self.radius = 0

    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
    def get_diameter(self):
        return self.diameter
    def set_diameter(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2



def main():
    circle1 = Circle()
    print(circle1.radius)
    print(circle1.radius)
    print(circle1.diameter)


main()