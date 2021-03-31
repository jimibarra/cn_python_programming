class Kangaroo:

    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        return f'The object {self.name} has the following item in its pouch: {self.pouch_contents}'

kanga = Kangaroo("first")
roo = Kangaroo("second")
kanga.put_in_pouch('apple')
kanga.put_in_pouch('orange')
kanga.put_in_pouch(roo)
print(kanga)
print(kanga.pouch_contents)
print(roo)









