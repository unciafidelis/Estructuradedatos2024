print("Dame el valor de n")
n = int(input())

c=1
p=2
d=2
while c <= n:
    if p % d == 0:
        print (p)
        c += 1
    d = 2
    p += 1
d += 1     
    