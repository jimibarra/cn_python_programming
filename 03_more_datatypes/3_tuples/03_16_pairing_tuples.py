'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
#Get list of numbers
print("Please enter a series of numbers and type quit when finished")
flag = True
my_list = []
while flag:
    num = input("Enter a number: ")
    if num == 'quit':
        break
    my_list.append(int(num))

#Sort the list
my_list.sort()

#Get length of list, determine if even or odd.  If odd append 0 to end of list
if len(my_list) % 2 == 0: # length is even
    pass
else:  # length is odd
    my_list.append(0)
print(my_list)

#Create list of tuples each with 2 items
num_interations = int((len(my_list)/2) -1)
new_list = []
count = 1

for x in range(1,num_interations +1):
    new_list.append(tuple(my_list[(count-1):(count+1)]))
    count += 2

new_list.append(tuple(my_list[-2:]))
print(new_list)

#Print each tuple
for tuple in new_list:
    print(tuple)



