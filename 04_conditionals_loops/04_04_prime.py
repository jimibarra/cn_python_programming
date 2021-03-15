'''
Print out every prime number between 1 and 100.

'''
#Create list of numbers to check
numbers = []
for x in range(2,101):
    numbers.append(x)

#Iterate over list.  Check each number to determine if prime.
#Write prime numbers to new list
prime_list = []

for num in numbers:
    flag = True        # is a prime number
    for i in range(2,num):
        modulo = num % i
        if modulo == 0:
            flag = False
            break
        else:
            pass
    if flag == True:
        prime_list.append(num)
    else:
        pass

print(prime_list)

