class Point:
    '''Point Class'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    '''Class Rectangle'''

    def __init__(self, name, width, height, point):
        self.name = name
        self.width = width
        self.height = height
        self.point = point

    def __str__(self):
        return f'The rectangle {self.name} with width {self.width}, height {self.height} and corner ({self.point.x} , {self.point.y})'

    def move_rectangle(self, dx, dy):
        new_x = self.point.x + dx
        new_y = self.point.y + dy
        self.point = Point(new_x, new_y)

    def new_rectangle(self, name, dx, dy):
        new_x = self.point.x + dx
        new_y = self.point.y + dy
        new_point = Point(new_x, new_y)
        name = Rectangle(name, self.width, self.height, new_point)
        return name


point1 = Point(1,1)
print(point1)
rectangle1 = Rectangle('rectangle1', 3, 2, point1)
print(rectangle1)
rectangle1.move_rectangle(2,2)
print(rectangle1)
rectangle2 = rectangle1.new_rectangle('rectangle2',3, 3)
print(rectangle2)
print(type(rectangle2))




