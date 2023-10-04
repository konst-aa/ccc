# stub from https://codeforces.com/blog/entry/71884
import sys

from functools import reduce

input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.acc = (0, 0)
        self.visited = False


############ ---- Solution ---- ############
def solve():
    lines = inp()
    flat = [Node(0)]  # qute offset
    for l in range(lines):
        flat.append(Node(0))

    for l in range(lines - 1):
        parent, child = inlt()
        flat[parent].edges.append(flat[child])
        flat[child].edges.append(flat[parent])
    vals = inlt()
    for i, val in enumerate(vals, 1):
        flat[i].val = val

    king = flat[1]

    greed_sum = abs(king.val)
    q = [king]
    while q:
        curr = q.pop(0)
        curr.visited = True
        new = list(filter(lambda n: not n.visited, curr.edges))
        q.extend(new)

    print(greed_sum)


solve()
