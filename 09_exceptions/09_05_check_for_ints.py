'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    try:
        user_input = int(input('Please enter a number: '))
        print(f'You typed {user_input}.')
        break
    except ValueError:
        print('ValueError: You did not type a number.  Please try again.')


