'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
my_list = []

while True:
    try:
        file_name = input('Please enter a file name: ')
        with open(file_name, 'r') as fin:
            for line in fin:
                my_list.append(line.strip())
        break
    except IOError:
        print('IOError:  The file does not exist.  Please try again.')

for item in my_list:
    try:
        result = 100 + int(item)
        print(f'Adding 100 yields {result}.')
    except ValueError:
        print('ValueError: The line in the file is not a number.')





