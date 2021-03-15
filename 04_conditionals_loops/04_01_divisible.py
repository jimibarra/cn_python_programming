'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
num = int(input("Please enter a number between 1 and 1,000,000,000: "))
modulo = num % 3

if modulo == 0:
    print(f'The number {num} is divisible by 3 and the result is {num // 3}')
else:
    print("The number you entered is not divisible by 3")

