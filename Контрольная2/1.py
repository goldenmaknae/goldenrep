import re

with open('file.xml', encoding='utf-8') as f:
        text = f.read()
        list = f.readlines
        c = 0
        start = list.index('<teiHeader>')
        end = list.index('</teiHeader>')
        for i in range(len(list)):
            if start < i < end:
                c += 1
            else:
                c = c

with open('count.txt', 'w', encoding='utf-8') as f:
    f.write(c)
