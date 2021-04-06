import os


def get_files(directory):
    '''Returns a list of all the .mp3 files in directory'''
    mp3_list = []
    for (root,dirs,files) in os.walk(directory, topdown=True):
        for file in files:
            if '.mp3' in file:
                mp3_list.append(os.path.join(root, file))
    return mp3_list

def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    file_pipe = os.popen(cmd)
    result = file_pipe.readline()
    x = result.find('/')
    result = result[0:x]
    #print(result)
    file_pipe.close()
    return result

'''Writes the mp3 file names to a file called mp3.txt'''
content = get_files('/home/ubuntu/test_mp3')
content_w = "\n".join(content)
with open('/home/ubuntu/mp3.txt', 'w' ) as mp3_file:
    mp3_file.write(content_w)

content_dict = {}
for item in content:
    checksum = compute_checksum(item)
    #print(checksum)
    content_dict[item] = checksum
print(content_dict)

unique_dict = {}
dup_dict = {}
for (k,v) in content_dict.items():
    if v not in unique_dict.values():
        unique_dict[k] = v
    else:
        dup_dict[k] = v
print(f"Duplicate: {dup_dict}")
print(f"Unique: {unique_dict}")







