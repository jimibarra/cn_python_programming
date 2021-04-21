'''
Write a script with a function that demonstrates the use of *args.

'''

def my_function(arg1, *args):
    print(arg1)
    for item in args:
        print(item)

my_function("positional arg", "first", "second", "third")

