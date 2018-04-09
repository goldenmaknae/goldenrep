import re

def page(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()        
    return lines

def count(regex, links):
    n = 0
    for link in links:
        r = re.search(regex, link)
        if r:
            n += 1
    return n

def comparing(a, b):
    t = a/b
    print('Во сколько раз больше людей с фамилией на -дзе, чем с фамилией на -швили: ', t)
    return t

def main():
    file = page('names.html')
    shv = count('<a href.+?>[А-Я].+? [А-Я].+? [А-Я].+?швили</a>', file)
    dze = count('<a href.+?>[А-Я].+? [А-Я].+? [А-Я].+?дзе</a>', file)
    comparing(dze, shv)

if __name__ == '__main__':
    main()
