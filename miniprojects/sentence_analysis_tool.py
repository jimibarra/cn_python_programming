# Command line tool to analyze a sentence
sentence = 'I love to work with dictionaries!'

# Remove spaces
new_sentence = sentence.replace(" ", "")
length = len(new_sentence)
#print(f'Sentence length is: {length}')

# Initialize counters
lower_count = 0
upper_count = 0
punc_count = 0
num_count = 0

# Count characters in the string
for x in new_sentence:
    if not x.isalnum():
        punc_count += 1
    elif x.isdigit():
        num_count += 1
    elif x.isupper():
        upper_count += 1
    elif x.islower():
        lower_count += 1
    else:
        print(f'This character is not classified: {x}')

print(f'Total Characters: {length}')
print(f'Total Special Characters: {punc_count}')
print(f'Total Upper Characters: {upper_count}')
print(f'Total Lower Characters: {lower_count}')
print(f'Total Numbers: {num_count}')