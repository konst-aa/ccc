# Implement the following function
from functools import reduce

def molasses(n, c, l):
    pastes = {}
    compressor = [(c[0], l[0])]
    for letter, length in zip(c[1:],l[1:]):
        if compressor[-1][0] == letter:
            compressor[-1] = (letter, compressor[-1][1] + length)
        else:
            compressor += [(letter, length)]
    for letter, length in compressor:
        if letter not in pastes:
            pastes[letter] = {1:0}
        for i in range(2, length+1):
            if i not in pastes[letter].keys():
                pastes[letter][i] = -1
            pastes[letter][i] += (length // i)
    big = reduce(lambda acc, m: max(acc, max([((n-1) * pastes) for (n, pastes) in m.items()])), pastes.values(), 0)
    t = 1 if big else 0
    return sum(l) - big + t

tests = int(input().strip()) # Number of test cases
for test in range(tests):
    n = int(input().strip())
    c = input().strip().split(' ')
    l = input().strip().split(' ')
    l = [int(x) for x in l]
    print(molasses(n, c, l))
