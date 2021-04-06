from ingredients import Ingredient

class Soup:
    '''Class that models making soup'''

    def __init__(self, ingredients_list):  #pass a list of objects from the Ingredient class.  Each contains name and amount.
        self.ingredients_list = ingredients_list
        self.name = ""
        self.num_ingredients = len(self.ingredients_list)
        self.serves = 0

    def cook(self):
        total_amount = 0
        for ingredient in self.ingredients_list:
            self.name += ingredient.name
            total_amount += ingredient.amount
        self.serves = total_amount / self.num_ingredients

    def __str__(self):
        return f'Here is some {self.name} soup and it serves {self.serves}.'

t = Ingredient('tomato', 5)
p = Ingredient('potato', 7)
soup = Soup([t , p])
print(soup)
soup.cook()
print(soup)


