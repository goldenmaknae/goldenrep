import re

def read(filename):
    with open('_itartass1.xhtml', 'r', encoding='utf-8') as f:
        text = f.readlines()
        abb = re.findall('[А-Я]', f)
        print(abb)
        
