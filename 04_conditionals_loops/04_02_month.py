'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
user_input = int(input("Please enter a number from 1 to 12: "))

if user_input >= 1 and user_input <= 12:
    print(f'The number you entered {user_input} corresponds to the month of {months[user_input]}')
else:
    print(f'The number {user_input} you entered is not within the requested range.')


