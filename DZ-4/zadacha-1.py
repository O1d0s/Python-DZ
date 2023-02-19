n = int(input("Количество чисел 1-го списка: "))
m = int(input("Количество чисел 2-го списка: "))

nabor_1 = []
nabor_2 = []
print("Ведите числа для 1-го списка: ") 
for i in range(n):
    x = int(input())
    nabor_1.append(x)

print("Ведите числа для 2-го списка: ") 
for i in range(m):
    x = int(input())
    nabor_2.append(x)

print(nabor_1)
print(nabor_2)
nabor_1 = set(nabor_1)
nabor_2 = set(nabor_2)

if n > m:
    nabor = nabor_1.intersection(nabor_2)
else:
    nabor = nabor_2.intersection(nabor_1)

print(sorted(list(nabor)))
