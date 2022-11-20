from functools import reduce

def sol(n):
    return sum(map(int, str(reduce(lambda acc, i: acc*i, range(1,n+1)))))

print(sol(100))
