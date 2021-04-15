def add_items(first, second):
    return first + second

def read_file(filename):
    with open(filename, 'r') as fin:
        content = fin.read()
    return content

def write_file(filename, content):
    with open(filename, 'w') as fout:
        fout.write(content)

if __name__ == '__main__':
    result_add = add_items(4, 3)
    print(result_add)
    result_read = read_file('test2.txt')
    print(result_read)
    write_file('test1.txt', result_read )
