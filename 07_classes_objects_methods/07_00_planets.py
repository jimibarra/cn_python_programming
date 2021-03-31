'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    '''Class to model planets'''

    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f'The plant {self.name} has color {self.color} and exists in system {self.system}.'

earth = Planet('earth', 'blue', 'solar')
mars = Planet('mars', 'red', 'solar')
print(earth)
print(mars)


