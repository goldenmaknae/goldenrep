#5 вариант

import os

files = os.listdir()
folds = ''
number = 0

for i in range(0, len(files)):
    path = './' + files[i]
    valid = False
    if os.path.isdir(path):
        for symbol in files[i]:
            if symbol == ' ':
                valid = True
        if valid:
            number += 1
            folds += files[i] + ', '
            
print('Папок, название которых состоит из более чем одного слова: ', number)
help = folds.split(',')

del help[-1]
folds = ', '.join(help)

print('Названия этих папок: ', folds)
