class Point:
    '''Point Class'''

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Circle:
    '''Circle Class'''

    def __init__(self, name, point, radius):
        self.name = name
        self.point = point
        self.radius = radius

    def __str__(self):
        return f'The circle {self.name} has center ({self.point.x}, {self.point.y}) and radius {self.radius}'

    def point_in_circle(self, rpoint):
        flag = True
        if (rpoint.x not in range(self.point.x - self.radius, self.point.x + self.radius+1)) or (rpoint.y not in range(self.point.y - self.radius, self.point.y + self.radius+1)):
            flag = False
        return flag

point1 = Point(150, 100)
circle1 = Circle('circle1', point1, 75)
print(circle1)
point2 = Point(150, 180)
result = circle1.point_in_circle(point2)
print(result)

