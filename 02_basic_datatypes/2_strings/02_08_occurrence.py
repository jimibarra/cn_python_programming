'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

sentence = input('Please enter a sentence: ')
letter = input('Please enter a letter that is in the sentence: ')
result = sentence.find(letter)
print(result)

