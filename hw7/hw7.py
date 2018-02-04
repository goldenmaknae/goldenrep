#5 вариант

length = 0
count = 0

def words_from_file(text):
    with open ("text.txt", encoding = 'utf-8') as f:
        text = f.read()
        text = text.replace('-', '')
        text = text.replace(',', '').replace('.', '')
        text = text.lower()
        words = text.split()
    return words
words = words_from_file('text.txt')

for word in words:
    if word[-3:] == 'ous':
        count += 1
        length += len(word)
print('Количество прилагательных: ',count)
print('Средняя длина: ',(length / count))


