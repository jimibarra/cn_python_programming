class Food:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __lt__(self, other):
        if self.name < other.name:
            return True
        return False

apple = Food('apple', 10)
orange = Food('orange', 20)
grapes = Food('grapes', 30)

#print(apple < grapes)
#print(orange < grapes)
#print(grapes < orange)

class Class1:
    def __init__(self, x=5):
        self.x = x

class Class2(Class1):
    def __init__(self):
        super().__init__(x=5)
        self.y = 1

#b = Class2()
#print(b.y + b.x)

class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return f'Time is {self.hour}:{self.minute}:{self.second}'

time1 = Time(1,20,30)
#print(time1)



