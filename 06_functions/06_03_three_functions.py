'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def square_func(n):
    square = n * n
    return square

def sum_of_squares(my_list):
    squared_list = []
    for item in my_list:
        squared_list.append(square_func(item))
    sum_list = sum(squared_list)
    return sum_list

def message():
    num_list = []
    while True:
        user_input = input('Please enter a number or quit to end: ')
        if user_input == 'quit':
            break
        else:
            num_list.append(int(user_input))
    returned_sum = sum_of_squares(num_list)
    print(f'The sum of the squares of the numbers provided is: {returned_sum}')

message()


