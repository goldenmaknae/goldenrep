import re

def get_file():
    ht = ""
    with open("georgian.html","r",encoding="utf-8") as fl:
        ht = fl.read()
    return ht

def get_names(ht):
    new_html = re.sub(r"title=\"(.+?)\">(?:[а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я]+) ([а-яА-Я]+) ([а-яА-Я]+(?:(швили)|(дзе)))</a>",r"title=\"\1\">Галактион \2 \3</a>",ht)
    return new_html

def wrt(ht):
    with open("new.html", "w", encoding="utf-8") as f:
        f.write(ht)

def main():
    wrt(get_names(get_file()))

print('Done')

main()
