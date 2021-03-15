'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

user_string = input("Please enter a string: ")
my_list = user_string.split(" ")
print(my_list)
my_dict = {}

my_set = set(my_list)
for item in my_set:
    count = 0
    count = my_list.count(item)
    my_dict[item] = count

max_count = max(my_dict, key=lambda x: my_dict.get(x))
print(f'The word {max_count} appears the most at {my_dict[max_count]} times')



