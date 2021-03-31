'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
class Animal:
    '''Class to model amimals'''

    def __init__(self, group, species, char): #char is a dictionary wih keys: name, age and weight
        self.group = group
        self.species = species
        self.char = char
        self.index = -1

    def __str__(self):
        return f'Animal is a {self.group} of type {self.species} with characteristics {self.char}'

    def __lt__(self, other):
        if self.species < other.species:
            return True
        return False

    def __add__(self, other):
        sum = self.species + " and " + other.species
        return sum

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.char):
            raise StopIteration
        return self.char[self.index]

class Fruit:
    '''Class to model fruit'''

    def __init__(self, name, color, amount):
        self.name = name
        self.color = color
        self.amount = amount

    def __str__(self):
        return f'This is fruit of type {self.name} with color {self.color} and with amount {self.amount}.'

    def use_fruit(self, quantity):
        self.amount -= quantity

class Apple(Fruit):
    '''Class to model apples'''

    def __init__(self, name, color, amount, apple_type):
        super().__init__(name, color, amount)
        self.apple_type = apple_type

    def __str__(self):
        return f'This is an apple of type {self.apple_type} with color {self.color} and with amount {self.amount}.'

#Animal Class Tasks

#Create 2 instances of Animal Class
animal1_dict = {'name':'Rex', 'age':5, 'weight':50}
animal2_dict = {'name':'Caley', 'age':2, 'weight':15}
animal1 = Animal('mammel', 'dog', animal1_dict)
animal2 = Animal('mammel', 'cat', animal2_dict)
print(animal1)
print(animal2)

#Test Dunder Methods for <, + and iteration
print(animal1 < animal2)
print (animal2 < animal1)
print(animal1 + animal2)
for k,v in animal1.char.items():
    print(k , v)

#Change Attribute Values
animal2.species = 'feline'
print(animal2)
animal2.char['name'] = 'Buttons'
print(animal2)

#Fruit Class Tasks
fruit1 = Fruit('apple', 'red', 20)
fruit2 = Fruit('orange', 'orange', 15)
print(fruit1)
print(fruit2)
fruit2.color = 'yellow'
fruit1.use_fruit(10)
print(fruit1)
print(fruit2)

#Apple Class Tasks
apple1 = Apple('apple', 'red', 25, 'gala')
apple2 = Apple('apple', 'red', 10, 'envy')
print(apple1)
print(apple2)
apple2.color = 'green'
apple1.use_fruit(5)
print(apple1)
print(apple2)




