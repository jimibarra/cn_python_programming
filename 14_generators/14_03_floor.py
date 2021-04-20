'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

my_list = [ 1, 2, 1111, 2222, 3333, 3, 4, 5, 4444, 5555, 6, 7, 8, 9]
gen = (x for x in my_list if x % 1111 == 0)

for item in gen:
    result = item // 1111
    print(result)
