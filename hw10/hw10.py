#5 вариант

import re

a = ''
b = ''

with open('cucumber.html', 'r', encoding='utf-8') as sock:
    for line in sock:
        a = a + ' ' + line.replace('\n', '\n')
        
with open ("output.txt", 'w', encoding = 'utf-8') as f:
    f.write(a)
    
for line in a:
    match = re.findall(r'Семейство:+\D+\d+\D+\w', a)
    if match:
        rg = re.compile('[^а-яёА-яё ]')
        for line in match:
            b = b + ' ' + line.replace('\n', '\n')
        print(rg.sub('', b))
        with open("log.txt", "w", encoding = "utf-8") as g:
            g.write(reg.sub('', b))
        break
    else:
        print('Ошибка 404')
        break
                
                
