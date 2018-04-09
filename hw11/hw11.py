import re

def main():
    with open('dinosaurs.html', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'динозавр([а-я](?:[а-я])?)','кот\g<1>', text)
    text = re.sub(r'Динозавр([а-я](?:[а-я])?)','Кот\g<1>', text)
    with open('cats.txt', 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    main()

print('Done')
