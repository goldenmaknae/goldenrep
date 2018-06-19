import re
import os
start_path = '.'

def first(t):
    for files in os.walk(start_path):
        print(files)
        f = open(files, encoding="utf-8")
        text = f.read()
        list = re.findall("gr=\"[A-Z]{1,}", text)

    f.close()

with open('1.csv', 'x'):
    pass

def abb():
    start_path = "."
    for files in os.walk(start_path):
        print(files)
        f = open(files, encoding="utf-8")
        text = f.read()
        
        list = re.search("lex=([А-Я])", text)
        if r:
            list.append(list.group(1))
        f.close()
    return list

list = abb()
count = collections.counter(list)
