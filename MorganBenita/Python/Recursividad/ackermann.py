def ackermann(M,N):
    if M == 0:
        return N+1
    else:
        if N == 0:
            return ackermann(M-1,1)
        else:
            return ackermann(M-1,ackermann(M,N-1))

print(ackermann(2,2))