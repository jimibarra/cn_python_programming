# Sort list based on number in each tuple

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

# Create sorted list of the number in each tuple
my_list = []
for tup in unsorted_list:
    my_list.append(tup[1])

my_list.sort()
print(my_list)

# Create a dictionary of number:tuple
my_dict = {}
for tup in unsorted_list:
    my_dict[tup[1]] = tup

print(my_dict)

# Create sorted list of tuples using dictionary lookups
sorted_list = []
for num in my_list:
    sorted_list.append(my_dict[num])

print(sorted_list)

