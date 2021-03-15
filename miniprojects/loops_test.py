my_list = [1, 2, 3, 4, 5]

# 'break' ends the execution of the loop, skipping anything after
for num in my_list:
    if num % 3 == 0:
        break
    print(num)
print("finished 'break' part")

for num in my_list:
    if num % 3 == 0:
        continue
    print(num)
print("finished 'continue' part")

n = 10
while True:
    if n <= 0:
        print("Blastoff")
        break
    else:
        print(n)
        n -= 1

people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

# Change everything below here to use while loops instead
for person in people:
    to_print = ""
    for name in person:
        to_print += name + " "
    print(to_print)

count = 0
total = len(people)

while count < total:
    name_list = people[count]
    if len(name_list) == 2:
       to_print = name_list[0] + " " + name_list[1]
       print(to_print)
       count += 1
    if len(name_list) == 1:
       to_print = name_list[0]
       print(to_print)
       count += 1
print("We are done!")

