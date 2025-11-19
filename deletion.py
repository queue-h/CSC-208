import sys

class Square:
    num_squares = 1

    def __init__(self, width, color):
        self.square_num = Square.num_squares
        Square.num_squares += 1
        self.width = width
        self.color = color

    def __str__(self):
        return f"A square of size {self.width} and color {self.color}."


    def get_num_squares(self):
        return f"You have created {Square.num_squares} squares."

sq = Square(5, 'red')
sq1 = sq
print(sys.getrefcount(sq))