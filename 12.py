a = list(input('Ваш текст: '))
for i,sym in enumerate(a):
    sym = "".join(a[-i:])
    sym += "".join(a[:-i])
    print(sym)
    
