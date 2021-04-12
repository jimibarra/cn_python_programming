'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
dict = {'key1':'val1', 'key2':'val2'}
list_ = ["hello world!"]

try:
    print(dict['key3'])
except KeyError:
    print('A KeyError has occurred.')
try:
    print(list_[1])
except IndexError:
    print('An IndexError has occurred.')
