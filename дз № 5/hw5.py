#5 вариант

latinwords = []
word = input('Введите латинское слово: ')
if word == '':
    print('Вы ввели пустое слово')
else:
    while word != '':
        if word.endswith('tur') or word.endswith('ntur'):
            latin_words.append(word + '\n')
        word = input()
with open("text.txt", "a", encoding="utf-8") as f:
        f.write(word+"\n")
with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()
print(text)
