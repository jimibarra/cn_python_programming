'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

string1 = input('Please enter the first string: ')
string2 = input('Please enter the second string: ')
string3 = input('Please enter the third string: ')
len1 = len(string1)
len2 = len(string2)
len3 = len(string3)

print(f'{len1}, {string1}')
print(f'{len2}, {string2}')
print(f'{len3}, {string3}')

high_len = len1
high_string = string1

if len2 > high_len:
    high_len = len2
    high_string = string2

if len3 > high_len:
    high_len = len3
    high_string = string3

print(f'The longest string is: {high_len}, {high_string}.')


