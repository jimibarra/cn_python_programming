'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

#Total Vowel Count
vowel = ['a', 'e', 'i', 'o', 'u']
string = input('Please enter a string of characters: ')

count = 0

for i in string:
    if i in vowel:
        count = count + 1

print(f'The number of vowels in the string is {count}.')

#Count of Each Vowel

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for i in string:
    if i in vowel:
        if i == 'a':
            count_a = count_a + 1
        elif i == 'e':
            count_e = count_e + 1
        elif i == 'i':
            count_i = count_i + 1
        elif i == 'o':
            count_o = count_o + 1
        else:
            count_u = count_u + 1

print(f'Counts By Vowel - a:{count_a}, e:{count_e}, i:{count_i}, o:{count_o}, u:{count_u}')
