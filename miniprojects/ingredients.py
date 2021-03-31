class Ingredient:
  """Models an Ingredient."""
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

  def use(self, use_amount):
      '''Reduces the amount of ingedients available.'''
      self.amount -= use_amount

  def expire(self):
    """Expires the ingredient item."""
    print(f"whoops, these {self.name} went bad...")
    self.name = "expired " + self.name

  def __str__(self):
   return f"You have {self.amount} {self.name}."

# we can define new classes that take over all their superclasses' variables and methods:
class Spice(Ingredient):  # means it inherits from the Ingredient class

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def expire(self):
        if self.name == 'salt':
            print(f"{self.name} never expires! ask the sea!")
        else:
            print(f"eh... sorry but that {self.name} actually got bad!")
            self.name = "expired " + self.name

#p = Ingredient('peas', 12)
#print(p)
#s = Spice('salt', 200)
#print(s)  # no need to define __str__() again - it works!

#c = Ingredient('carrots', 3)
#p = Spice('pepper', 20)
#print(c, p)
#p.grind()
#c.grind()  # produces an error

#c = Ingredient('carrots', 3)
#p = Spice('pepper', 20)
#s = Spice('salt', 200)
#print(c, p, s)
#p.expire()
#print(p)
# try calling expire() with the c and s objects!
#c.expire()
#print(c)
#s.expire()
#print(s)

c = Ingredient('carrots', 3)
# p = Spice('pepper', 20)  # produces an error now
p = Spice('pepper', 20, 'spicy')
print(c, p)
print(p.taste)  # a new variable only in Spice objects!
# print(c.taste)  # doesn't exist!
