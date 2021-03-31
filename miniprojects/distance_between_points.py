import math

class Point:
    '''Class Points'''

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point {self.name} has x value {self.x} and y value {self.y}.'

point1 = Point('point1', 1, 2)
point2 = Point('point2', 3, 4)

print(point1)
print(point2)
distance = math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)
print(distance)




