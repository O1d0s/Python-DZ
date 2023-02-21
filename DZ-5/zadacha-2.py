a = int(input('a='))
b = int(input('b='))

def summa(a,b):
    if b == 0:
        return a
    else:
        a += 1
        return summa(a,b-1)
print(summa(a,b))