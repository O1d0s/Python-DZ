a1 = int(input('Введите первый элемент массива: '))
d = int(input('Введите разность чисел: '))
n = int(input('Введите длинну массива: '))

arif = []

an = a1 + (n-1)*d

for i in range(a1,an,d):
    arif.append(i)

print(arif)