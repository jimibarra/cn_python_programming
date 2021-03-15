'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
#Build the list
my_list = []

for x in range(10):
    num = int(input("Please enter a number: "))
    my_list.append(num)

#Print even positions in order
for even in range(2,11,2):
    print(my_list[even-1])

#Print odd positions in reverse order
my_list.reverse()
for even in range(2,11,2):
    print(my_list[even-1])


