'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(sequence):
      my_list = []
      count = 0
      for item in sequence:
          my_tuple = (count, item)
          my_list.append(my_tuple)
          count +=1
      return my_list

my_list = ['a', 'b', 'c', 'd']
result = my_enumerate(my_list)
print(result)
