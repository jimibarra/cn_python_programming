#a = 0
#b = 42
#breakpoint()
#a += b
#breakpoint()

my_list = [1, 22, 3, 5, 42]
new_list = []
for x in my_list:
   #breakpoint()
   print(x)
   x += 1
   print(x)
   new_list.append(x)
print(new_list)


