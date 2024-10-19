def catalan(N):
    if N == 0:
        return 1
    else:
        S = 0
        for I in range(N):
            S += catalan(I)*catalan(N-I-1)
        return S
    
print(catalan(5))