'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    '''Class to model cars'''

    def __init__(self, model, year, max_speed=60):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f'The car is a {self.year} {self.model} with a max speed of {self.max_speed}.'

    def increment_max_speed(self):
        self.max_speed += 5

j_car = Car('BMW Z3', 1998)
d_car1 = Car('BMW Z3', 2001)
d_car2 = Car('Jaguar VP', 2005, 70)

print(j_car)
print(d_car1)
print(d_car2)

j_car.increment_max_speed()
j_car.increment_max_speed()
print(j_car)

d_car2.increment_max_speed()
d_car2.increment_max_speed()
d_car2.increment_max_speed()
print(d_car2)

d_car2.year = 2008
print(d_car2)



