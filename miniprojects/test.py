gen = (x for x in range(5))  # looks similar to a list comprehension!

print(gen)  # however, it's a "generator object" - no items are saved in memory

for i in gen:  # we can iterate over it
  print(i)
  








