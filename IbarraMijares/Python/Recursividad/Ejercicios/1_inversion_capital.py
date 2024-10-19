def Capital(m,X,n):
    if n==0:
        return m

    else:
        CapitalConInteres = m*(1+X/100)
        return Capital(CapitalConInteres,X,n-1)

m = 100000
X = 15
n = 10
print(Capital(m,X,n))