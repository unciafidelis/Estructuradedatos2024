def capitalIter(m,X,n):
    for _ in range(n):
        m+=m*(X/100)
    return m

m = 100000
X = 15
n = 10

print(capitalIter(m,X,n))