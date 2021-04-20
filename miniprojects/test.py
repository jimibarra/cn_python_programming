#courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

#for i, c in enumerate(courses):
    #print(f"{i}: {c} python")

  
def my_enumerate(sequence):  #sequence is a sequence of items (list, tuple, string).
  count = 0
  my_list = []
  for item in sequence:
    my_tuple = (count, item)
    my_list.append(my_tuple)
    count += 1
  return my_list

sequence = ['a', 'b', 'c', 'd']
result = my_enumerate(sequence)
print(result)









