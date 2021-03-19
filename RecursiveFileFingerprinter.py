from hashlib import md5
import os
import json
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


nickname = 0
seen = {}
exclude = [".git", "node_modules"]


def set_next(directory):
    global nickname
    if directory in seen:
        return seen[directory]["nickname"]
    else:
        nickname += 1
        seen[directory] = {}
        seen[directory]["nickname"] = nickname
        seen[directory]["children"] = []


def add_child_into_directory(directory, filename, fingerprint):
    if directory not in seen:
        set_next(directory)
    nn = seen[directory]["nickname"]
    obj = {}
    obj["filename"] = filename
    obj["fingerprint"] = fingerprint
    obj["parent"] = nn

    seen[directory]["children"].append(obj)


for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude]
    path = root.split(s)
    for file in files:

        file_base = os.path.join(root, file)
        hash = fingerprinter(file_base)
        pretty = len(path) * '---'
        # print("{}{} : {}".format(pretty, file, hash))
        # add_child_into_directory( file_)
        # print(path)
        if file.endswith(".js") or file.endswith(".py"):
            add_child_into_directory(root, file, hash)

print(seen)
print("The end")
