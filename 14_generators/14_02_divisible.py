'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

my_list = [ 1, 2, 1111, 2222, 3333, 3, 4, 5, 4444, 5555, 6, 7, 8, 9]
gen = (x for x in my_list if x % 1111 == 0)

for item in gen:
    print(item)

