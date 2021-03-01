'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

#Get sentence from user
sentence = input('Please provide a sentence: ')
#Get symbol from user
symbol = input('Please provide a symbol: ')
#Determine first letter of sentence
first = sentence[0]
#Replace each occurrence of first letter with symbol
new_sentence = sentence.replace(first,symbol)
print(new_sentence)


