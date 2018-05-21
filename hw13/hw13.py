import os

start_path = '.'

for root, dirs, files in os.walk(start_path):
    print('Где мы находимся: ', root)
    print('Папки: ', dirs)
    print('Файлы: ', files)

filenames = {}
for file in files:
    filenames[os.path.splitext(file)[0]] = 0

print('Сколько в этих папках встречается разных названий файлов без учёта расширений: ', len(filenames))
