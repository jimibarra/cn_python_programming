'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# Get string from user
my_string = input("Please type a sentence: ")

# Create a list where items are each word from the string
list_words = my_string.split(" ")
#print(list_words)

# Create a list where each item is a tuple of each word
list_tuples = []
for word in list_words:
    list_tuples.append(tuple(word))
print(list_tuples)



