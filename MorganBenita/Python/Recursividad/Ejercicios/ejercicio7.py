def p1(x):
    if x>100:
        return x-8
    else:
        return p1(p1(x+9))

print(p1(38))
print(p1(51))
print(p1(24))
