'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
#Get the string
my_string = input("Please enter a string: ")

#Break string into a list
my_list = []
for x in my_string:
    my_list.append(x)

#Create a set from the list
my_set = set(my_list)
my_set = sorted(my_set)

#Iterate over set and count letters in list.  Place item and count in dictionary
my_dict = {}
for item in my_set:
    count = 0
    count = my_list.count(item)
    my_dict[item] = count
print(my_dict)

