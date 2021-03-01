'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

import math

pi = math.pi
radius = 3.14
height = 5

volume = pi*(radius**2)*height
print(f'The volume of the cylander is: {volume}')
surface_area = (2*pi*radius*height) + (2*pi*(radius**2))
print(f'The surface area of the cylander is: {surface_area}')

