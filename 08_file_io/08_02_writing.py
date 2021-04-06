'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

'''Read in contents of file and create reversed list of words.'''
with open('words.txt', 'r') as fin:
    word_list = []
    for word in fin:
        word_list.append(fin.readline())
    word_list.reverse()

'''Write the contents of the reversed list to a file'''
with open('words_reverse.txt', 'w') as fout:
    for word in word_list:
        fout.write(word)





