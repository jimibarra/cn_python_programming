'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def func_or(num):
    result_4 = num % 4
    result_7 = num % 7
    if result_4 == 0 or result_7 == 0:
        return True
    else:
        return False


def func_and(num):
    result_4 = num % 4
    result_7 = num % 7
    if result_4 == 0 and result_7 == 0:
        return True
    else:
        return False

user_input = int(input("Please enter a number between 1 and 1,000,000,000: "))

or_result = func_or(user_input)
and_result = func_and(user_input)

print(f'The result for the "Or" test is {or_result}')
print(f'The result for the "And" test is {and_result}')


