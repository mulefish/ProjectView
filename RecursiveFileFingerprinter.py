from hashlib import md5
import os
import json
from get_id import get_id
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


def add_next_directory(directory):
    global nickname
    if directory in seen:
        return seen[directory]["nickname"]
    else:
        nickname += 1
        seen[directory] = {}
        seen[directory]["nickname"] = get_id(nickname)
        seen[directory]["files"] = []
        seen[directory]["daughters"] = []
        seen[directory]["daughters_nicknames"] = []


def add_file_into_directory(directory, filename, fingerprint):
    if directory not in seen:
        add_next_directory(directory)

    nn = seen[directory]["nickname"]
    obj = {}
    obj["filename"] = filename
    obj["fingerprint"] = fingerprint
    obj["parent"] = nn

    seen[directory]["files"].append(obj)


for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude]
    path = root.split(s)
    for file in files:
        file_base = os.path.join(root, file)
        hash = fingerprinter(file_base)
        if file.endswith(".js") or file.endswith(".py"):
            add_file_into_directory(root, file, hash)


for directory_name in seen:
    nickname = seen[directory_name]["nickname"]
    path = directory_name.split(os.sep)
    path.pop()
    parent_name = os.sep.join(path)
    seen[directory_name]["parent"] = parent_name
    if parent_name in seen:
        print("yay " + parent_name + " and " + nickname)
        seen[parent_name]["daughters_nicknames"].append(nickname)
        seen[parent_name]["daughters"].append(directory_name)
    else:
        print("boo " + parent_name)

    #seen[directory_name]["parent_nickname"] = seen[parent_name]["nickname"]
    # print(seen[directory_name])
print(seen)
