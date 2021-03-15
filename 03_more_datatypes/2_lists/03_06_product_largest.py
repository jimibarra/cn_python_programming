'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
# Build the list
my_list = []
prod = 1
for x in range(10):
    num = int(input("Please enter a number: "))
    my_list.append(num)
    prod *= num


largest = max(my_list)
print(f'The largest number is:  {largest}')
print(f'The product of the numbers is:  {prod}')

