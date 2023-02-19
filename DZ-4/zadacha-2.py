n = int(input("Введите количество кустов в грядке: "))

my_list = []
print("Введите количество ягод в каждом кусте:")
for i in range(n):
    x = int(input())
    my_list.append(x)

print(my_list)
s=0
for i in range(1,n):
    if i-1 == 0:
        if my_list[n-1]+my_list[i-1]+my_list[i] > s:
            s = my_list[n-1]+my_list[i-1]+my_list[i]
    elif i == n-1:
        if my_list[i-1]+my_list[i]+my_list[n-(i+1)] > s:
            s = my_list[i-1]+my_list[i]+my_list[n-(i+1)]
    else:
        if my_list[i-1]+my_list[i]+my_list[i+1] > s:
            s = my_list[i-1]+my_list[i]+my_list[i+1]

print(s)
