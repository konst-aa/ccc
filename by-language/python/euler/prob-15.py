from functools import reduce

def paths(n):
    t_acc = lambda acc, i: acc * i
    def fac(n):
        return reduce(t_acc, range(1, n+1))

    a = reduce(t_acc, range(n+1, 2*n + 1))
    return a // fac(n)


print(paths(20))
