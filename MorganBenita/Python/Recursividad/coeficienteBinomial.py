def CB(N,K):
    if K==0 or N==K:
        return 1
    else:
        return CB(N-1,K-1)+CB(N-1,K)

print(CB(5,2))