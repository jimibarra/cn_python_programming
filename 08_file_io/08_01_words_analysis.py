'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

def find_min(filename):
    '''Find the min length of words in a file'''

    min = 20
    with open(filename, 'r') as fin:
        for word in fin:
            length = len(word.strip())
            if length < min:
                min = length
    return min

def find_max(filename):
    '''Find the max length of words in a file'''

    max = 1
    with open(filename, 'r') as fin:
        for word in fin:
            length = len(word.strip())
            if length > max:
                max = length
    return max



def print_length(filename, word_len):
    with open(filename, 'r') as fin:
        for word in fin:
            length = len(word.strip())
            if length == word_len:
                print(word.strip())


if __name__ == '__main__':

    '''Print words with min length in file'''
    min_length = find_min('words.txt')
    print_length('words.txt', min_length)

    '''Print words with max length in file'''
    max_length = find_max('words.txt')
    print_length('words.txt', max_length)

    '''Determine the number of words in the file'''
    with open('words.txt', 'r') as fin:
        words = []
        for word in fin:
            words.append(word)
        print(f'There are {len(words)} words in the file.')



