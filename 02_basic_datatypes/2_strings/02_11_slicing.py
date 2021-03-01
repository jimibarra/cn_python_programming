'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name = input("Please type your name: ")
first = name[0]
pg_name = name[1:]
pg_name = pg_name + first
pg_name = pg_name + 'ay'
print(pg_name)

