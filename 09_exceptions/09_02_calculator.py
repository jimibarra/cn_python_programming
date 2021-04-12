'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

try:
    x = int(input('Please enter dividend: '))
    y = int(input('Please enter divisor: '))
    print(f'The quotient is: {x / y}')
except ZeroDivisionError:
    print('Please enter a nonzero divisor.')
except ValueError:
    print('Please enter a number, not a word or letter.')
else:
    print("Successfully performed the division.")
finally:
    print('This is the end of this round.')





