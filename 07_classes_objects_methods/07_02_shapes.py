'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math

class Rectangle:
    '''Class to model a rectangle '''

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f'Rectangle has length {self.length} and width {self.width}.'

    def area_rect(self):
        area_r = self.length * self.width
        return area_r

    def perim_rect(self):
        perim_r = (2 * self.length) + (2 * self.width)
        return perim_r

class Circle:
    '''Class to model a circle'''

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle has radius {self.radius}.'

    def area_circle(self):
        area_c = math.pi * (self.radius ** 2)
        return area_c

    def circum_circle(self):
        circum_c = 2 * math.pi * self.radius
        return circum_c

my_rect = Rectangle(3, 4)
my_circ = Circle(5)
print(my_rect)
print(my_circ)

print (f'The area of the rectangle is {my_rect.area_rect()}.')
print (f'The perimeter of the rectangle is {my_rect.perim_rect()}.')
print (f'The area of the circle is {my_circ.area_circle()}.')
print (f'The circumference of the circle is {my_circ.circum_circle()}.')


