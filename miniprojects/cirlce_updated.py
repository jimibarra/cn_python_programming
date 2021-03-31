import math
from rectangle import Rectangle
import copy

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

def distance_between_points(point1, point2):
    distance = 0
    distance = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
    return distance

def point_in_circle(rcircle, rpoint):
    d = 0
    d = distance_between_points(rcircle.point, rpoint)
    flag = True
    if d > rcircle.radius:
        flag = False
    return flag

def rect_in_circle(rcircle, rrect):
    p = copy.copy(rrect.point)
    if not point_in_circle(rcircle, p):
        return False
    p.y += rrect.height
    if not point_in_circle(rcircle, p):
        return False
    p.x += rrect.width
    if not point_in_circle(rcircle, p):
        return False
    p.y -= rrect.height
    if not point_in_circle(rcircle, p):
        return False
    return True


c_point = Point(1, 1)
t_circle = Circle('test_circle', c_point, 3)
t_point = Point(3, 4)
r_point = Point(1 ,1)
t_rectangle = Rectangle('test_rectangle', 1, 1, r_point)

print(t_circle)
dist_point = distance_between_points(c_point, t_point)
print(f'Distance between circle center and point is {dist_point}')

p_in_c = point_in_circle(t_circle, t_point)
print(f'Result of is point in circle: {p_in_c}')

print(t_rectangle)
r_in_c = rect_in_circle(t_circle, t_rectangle)
print(r_in_c)

