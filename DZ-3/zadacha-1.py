import random

n = int(input("Напишите длину списка: "))

spisok = [random.randint(1,100) for i in range(1,n+1)]

print(spisok)
x = int(input("Введите число Х: "))
count=0
min_blizko = abs(x - spisok[0])
index = 0
for i in range(n):
    if spisok[i] == x:
        count+=1
    elif abs(x - spisok[i]) < min_blizko:
        min_diffmin_blizko = abs(x - spisok[i])
        index = i


if count>0:
    print(count)
else:
    print(spisok[index])


