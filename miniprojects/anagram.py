from anagram_sets import all_anagrams
import shelve

def store_anagrams(ana_dict):
    shelf = shelve.open('shelve_file', 'c')
    for (k,v) in ana_dict.items():
        shelf[k] = v
    shelf.close()

def read_anagrams(word_key):
    shelf = shelve.open('shelve_file')
    result = shelf[word_key]
    shelf.close()
    return result

if __name__ == '__main__':

    #anagram_map = all_anagrams('words.txt')
    #store_anagrams(anagram_map)
    lookup_result = read_anagrams('opst')
    print(lookup_result)
