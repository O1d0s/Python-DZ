from random import randint

n = int(input('Введите длинну массива: '))
a,b = map(int, input('Введите начало и конец диапазона чисел через пробел: ').split())
spisok = []

for i in range(n):
    spisok.append(randint(0,50))

print(spisok)

index = []

for i in range(n):
    if a<spisok[i]<b:
        index.append(i)

print(index)
