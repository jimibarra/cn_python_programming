'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def my_sum(sequence): #the sequence argument is a list of numbers.
    sum = 0
    for item in sequence:
        sum += item
    return sum

my_list = [100, 10, 20, 30 , 40 , 50]
result = my_sum(my_list)
print(f'The sum of the list provided is {result}.')

