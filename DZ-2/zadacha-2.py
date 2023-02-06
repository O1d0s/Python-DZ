x = int(input("Напишите сложение 2 чисел: "))
y = int(input("Напишите умножение 2 чисел: "))
for i in range(x):
    for j in range(y):
        if i + j == x and i*j==y:
            print(i)
            print(j)
            break
        else:
            print("Не правильно указано сложение и умножение чисел")
            break