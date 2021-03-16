secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

#Create a dictionary of letters to number
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_dict = {}
count = 1
for char in alphabet:
    alpha_dict[char] = count
    count += 1
print(alpha_dict)

#Create a list of letters of the alphabet
alpha_list = list(alphabet)
print(alpha_list)

#Look up the cipher and create cipher list
cipher_list = []
for char in secret:
    if not char.isalnum():
        cipher_list.append(char)
    else:
        lookup = alpha_dict[char.lower()]
        if lookup <= 19:
            index = lookup + 6
            cipher_letter = alpha_list[index]
            cipher_list.append(cipher_letter)
        else:
            index = lookup - 20
            cipher_letter = alpha_list[index]
            cipher_list.append(cipher_letter)

print(cipher_list)

#Create cipher string
cipher_string = "".join(cipher_list)
print(cipher_string)


