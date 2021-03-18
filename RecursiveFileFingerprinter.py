from hashlib import md5
import os
s = os.sep

# fingerprinter from:
# https://stackoverflow.com/questions/65372048/is-there-a-fast-way-to-fingerprint-a-large-number-of-files-in-python
# downwithocp
# asked Dec 19 '20 at 16:37
BLOCK_SIZE = 65536


def fingerprinter(file_path):
    hash_method = md5()
    with open(file_path, 'rb') as input_file:
        buf = input_file.read(BLOCK_SIZE)
        while len(buf) > 0:
            hash_method.update(buf)
            buf = input_file.read(BLOCK_SIZE)

    return hash_method.hexdigest()


for root, dirs, files in os.walk('.'):
    path = root.split(s)
    print(root)
    for file in files:
        file_base = os.path.join(root, file)
        hash = fingerprinter(file_base)
        pretty = len(path) * '---'
        print("{}{} : {}".format(pretty, file, hash))

print("The end")
