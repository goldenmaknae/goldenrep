def read(filename):
    with open('mystem.xml', encoding='utf-8') as f:
        text = f.read()
        list = text.split('\n')
        c = 0
        start = list.index('<se>')
        end = list.index('</se>')
        for i in range(len(list)):
            if start < i < end:
                c += 1
            else:
                c = c
        return c

with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(str(read('mystem.xml')))
