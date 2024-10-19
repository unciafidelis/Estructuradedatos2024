def capital(m,X,n):
    if n==0:
        return m
    else:
       capitalConInteres = m*(1+X/100) 
       return capital(capitalConInteres,X,n-1)

m = 100000
X = 15
n = 10

print(capital(m,X,n))
