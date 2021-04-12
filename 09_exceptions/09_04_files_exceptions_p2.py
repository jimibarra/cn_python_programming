'''

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
import os

class PrinceError(Exception):
    pass

def first_char(filename): #argument is relative path to file
    with open(filename, 'r') as fin:
        first_line = fin.readline()
        char = first_line[0]
        return char

def prince(filename): #argument is relative path to file
    with open(filename, 'r') as fin:
        first_hund = ""
        for line in fin:
            first_hund += line
            if len(first_hund) < 100:
                continue
            else:
                break
        first_hund = first_hund[0:101]
        #print(first_hund)
        if "Prince" in first_hund:
            return True
        else:
            return False


'''Print first character in a list of books.'''
files = os.listdir('books')
path = 'books'
for file in files:
    book = file
    full_path = path + '/' + book
    try:
        first = first_char(full_path)
        print(f'The first character in {book[0:-4]} is {first}')
    except IndexError:
        print(f'The book {book[0:-4]} has no content.')

'''Determine which books have Prince in first 100 characters'''
for file in files:
    book = file
    full_path = path + '/' + book
    try:
        response = prince(full_path)
        if response == False:
            print(f'The book {book[0:-4]} does not contain the word Prince.')
        else:
            raise PrinceError
    except PrinceError:
        print(f'PrinceError: The book {book[0:-4]} contains the word Prince.')




