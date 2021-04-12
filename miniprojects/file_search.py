'''Creates a list of the files in a directory with a given extension.'''

import os

def find_all(dir): #directory to search
    '''Find all files in a specific directory'''

    file_list = []
    for (root, dirs, files) in os.walk(dir, topdown=True):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def find_files(dir, ext): #directory to search and extension including "."
    '''Find files with a specific extension'''

    file_list = []
    for (root, dirs, files) in os.walk(dir, topdown=True):
        for file in files:
            if ext in file:
                file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':

    '''Find .jpg files'''
    directory = '/home/ubuntu/test_mp3'
    extension = '.jpg'
    my_list = find_files(directory, extension)
    #print(my_list)

    '''Find all file types specified in a list'''
    directory = '/home/ubuntu/test_mp3'
    extension_list = ['.txt', '.jpg', '.mp3']

    for type in extension_list:
        my_list = []
        my_list = find_files(directory, type)
        #print(my_list)

    '''Find all files.  Create list of extensions.  Create list of files for each extension'''
    my_list = []
    my_list = find_all(directory)
    #print(my_list)

    extension_list = []
    for item in my_list:
        ext = item[-4:]
        extension_list.append(ext)
    extension_list = list(set(extension_list))
    #print(extension_list)

    for type in extension_list:
        my_list = []
        my_list = find_files(directory, type)
        print(my_list)






