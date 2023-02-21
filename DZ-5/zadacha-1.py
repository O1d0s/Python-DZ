a = int(input('a='))
b = int(input('b='))
s = 1
def stepen(a,b,s):
    if b == 0:
        return 1
    elif b == 1:
        return s
    else:
        s *= a 
        return stepen(a,b-1,s)
print(stepen(a,b+1,s))