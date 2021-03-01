'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#Convert int to float
integer = 3
float_number = float(integer)
print(float_number)

#Convert float to int
float_number = 3.5
integer = int(float_number)
print(integer)

#Floor Division
integer = 3
float_number = 3.5
division_result = float_number / integer
print(division_result)

#Multiplication
first = float(input('Please enter first number: '))
second = float(input('Please enter second number: '))
product = first * second
print(f'The result of the multiplication is {product}')

