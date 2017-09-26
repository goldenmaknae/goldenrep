a = int(input())
b = int(input())
c = int(input())

if a % b == c:
    print('Удовлетворяет условию')
elif a*c+b == 0:
    print('Удовлетворяет условию')
else:
    print('Не удовлетворяет условию')
