'''
Write a script that demonstrates a try/except/else.

'''
'''Create a list from a sequence of numbers.'''

try:
    sequence = input('Please enter a sequence of numbers with no separators: ')
    my_list = list(sequence)
    for item in my_list:
        if item.isdigit() == False:
            raise ValueError
    print(my_list)
except ValueError:
    print('The sequence must consist of numbers only.  Please enter the sequence again.')
else:
    print('Successfully created a list of numbers.')
finally:
    print('End of this round.')

