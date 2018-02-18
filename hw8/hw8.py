import random

attempts = 0

def guess_words(filename):
	d = {}
	with open(filename, encoding = 'utf-8') as f:
		for line in f:
			line = line.strip()
			splited_line = line.split(',')
			d[splited_line[0]] = splited_line[1]
	return d

d = guess_words('words.csv')
words = list(d.keys())
word = random.choice(words)	
print('Отгадайте слово! Подсказка: ', word, '...')
answer = input('Ответ: ')
if answer == d[word]:
    print('Вы выиграли!')
else:
    attempts += 1
    print('Вы проиграли. Попыток сделано: ', attempts)
