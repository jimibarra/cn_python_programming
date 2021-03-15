'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
my_list = [1]
for num in range(2,101):
    if num % 2 == 1:
        my_list.append(num)
    else:
        pass
for x in my_list:
    print(x)
