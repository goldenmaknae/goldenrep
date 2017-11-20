import sys
 
badChars = ",.!'\":;-"
def onlyChars(word):
    for c in badChars:
        word = word.replace(c,'')
    return word
 
with open("kpop.txt", encoding="utf-8") as h:
    words = list(filter(lambda w: w != '',map(onlyChars,h.read().split())))
    gt = len(list(filter(lambda w: len(w) > 10, words)))
    total = len(words)
    print('Слов длины больше 10: ', '%d%%' % (100 * gt / total))
