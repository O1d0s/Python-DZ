n=int(input())
res=0
for i in range(n):
    res = 2**i
    if res > n:
        break
    print(res)