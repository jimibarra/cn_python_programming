class Letter:

    def __init__(self):
        self.mystring = 'abcdefg'
        self.mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.mydict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,}
        self.index = -1

    def __len__(self):
        return len(self.mydict)

    #def __getitem__(self, index):
        #return self.mylist[index]

    def __setitem__(self, index, value):
        self.mydict[index] = value

    def __delitem__(self, index):
        del self.mydict[index]

    def __iter__(self):
        return self

    def __next__(self):
       self.index += 1
       if self.index == len(self.mylist):
            raise StopIteration
       return self.mylist[self.index]

letter1 = Letter()
#print(len(letter1))
#result = letter1[2]
#print(result)
#letter1['b'] = 7
#print(letter1.mydict)
#del letter1['a']
#print(letter1.mydict)
#print(letter1.mydict.items())
#print(letter1[1])
for x in letter1.mydict.items():
    print(x)














