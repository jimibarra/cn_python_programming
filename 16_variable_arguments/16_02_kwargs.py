'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_function(arg1, **kwargs):
    print(arg1)
    for k,v in kwargs.items():
        print(f"Name is {k} and value is {v}.")

my_function("positional arg", first=1, second=2, third=3)
