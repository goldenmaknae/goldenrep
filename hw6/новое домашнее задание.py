import random

def imperative():
    with open("imperative.txt", encode = "utf-8") as f:
        imperatives = f.read()
        imperatives = imperatives.split()
    return random.choice(imperative)

def verb():
    with open("verb.txt", encode = "utf-8") as f:
        plural_verbs = f.read()
        plural_verbs = plural_verbs.split()
    return random.choice(plural_verbs)

def noun_phrase():
    with open("clitic.txt", encode = "utf-8") as f:
        clitics = f.read()
        clitics = clitics.split()
    clitic = random.choice(clitics)
    with open("word.txt", encode = "utf-8") as f:
        words2 = f.read()
        words2 = words2.split()
    noun = random.choice(words2)
    return clitic + ' ' + noun

def noun(number):
    with open("singular_noun.txt", encode = "utf-8") as f:
        singular_nouns = f.read()
        singular_nouns = singular_nouns.split()
    with open("plural_noun.txt", encode = "utf-8") as f:
        plural_nouns = f.read()
        plural_nouns = plural_nouns.split()
    if number == 's':
        return random.choice(singular_nouns)
    return random.choice(plural_nouns)

def ssp():
    with open("ssp.txt", encode = "utf-8") as f:
        ssps = f.read
        ssps = ssps.split()
    return random.choice(ssps)

def spp():
    with open("spp.txt", encode = "utf-8") as f:
        spps = f.read
        spps = ssps.split()
    return random.choice(spps)

def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def verse1():
    return noun('pl') + ' ' + verb() + ',' + ' ' + ssp() + ' ' + noun('pl') + punctuation()

def verse2():
    return imperative() + ' ' + noun('s') + ',' + ' ' + spp() + ' ' + noun_phrase() + punctuation()

def verse3():
    return noun_phrase() + ' ' + verb() + + ',' + ' ' + ssp() + noun('pl') + punctuation()

def verse4():
    return noun('pl') + ' ' + verb() + ',' + ' ' + ssp() + ' ' + noun('pl') + punctuation()

def verse5():
    return imperative() + ' ' + noun('s') + ',' + ' ' + spp() + ' ' + noun_phrase() + punctuation()


def make_verse():
    verse = random.choice([1,2,3,4,5])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()
 
for n in range(5):
    print(make_verse())
