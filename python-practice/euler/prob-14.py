def rule(n):
    return n//2 if n%2 == 0 else (3*n + 1)

m = 0
b = 0
for i in range(4, 10**6):
    n = i
    c = 1
    while n != 1:
        c+=1
        n = rule(n)
    if c > m:
        b = i
        m = c
print(b)
