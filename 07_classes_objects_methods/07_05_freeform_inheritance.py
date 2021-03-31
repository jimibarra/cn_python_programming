'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class Restaurant:
    '''Class to model restaurants'''

    def __init__(self, name, location, size):
        self.name = name
        self.location = location
        self.size = size

    def __str__(self):
        return f'The restaurant {self.name} is located in {self.location} and has size {self.size}.'

class Gourmet(Restaurant):
    '''Class to model gourmet restaurants'''

class FastFood(Restaurant):
    '''Class to model fast food restaurants'''

    def __init__(self, name, location, size, chain_name):
        super().__init__(name, location, size)
        self.chain_name = chain_name

    def __str__(self):
        return f'The restaurant {self.name} is located in {self.location}, has size {self.size} and is part of chain {self.chain_name}.'

class Michelin(Gourmet):
    '''Class to model Michelin restaurants'''

    def __init__(self, name, location, size, ethnicity):
        super().__init__(name, location, size)
        self.ethnicity = ethnicity

    def __str__(self):
        return f'The restaurant {self.name} is located in {self.location}, has size {self.size} and has ethnicity {self.ethnicity}.'


rest1 = Restaurant('La Grotta', 'Atlanta', 'small')
print(rest1)
gour1 = Gourmet('Soto Soto', 'Atlanta', 'small')
print(gour1)
ff1 = FastFood('Burger King - Ponce', 'Atlanta', 'small', 'Burger King')
print(ff1)
mich1 = Michelin('Ecco', 'Atlanta', 'small', 'Italian')
print(mich1)



