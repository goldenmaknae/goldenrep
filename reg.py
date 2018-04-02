import re

def text_read():
    with open('ling.txt', encode='utf-8') as f:
        text = f.read()
    return text

def tag_delete():
    with open('ling.txt', encode='utf-8') as f:
        plain_text = re.sub('<.+?>', '')
    return plain_text

print plain_text
