# stub from https://codeforces.com/blog/entry/71884
import sys

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


# solving: https://codeforces.com/problemset/problem/1687/A


def solve():
    num_tests = inp()
    for x in range(num_tests):
        mushroom_slots, time = inl()
        field = inl()
        if mushroom_slots <= time:
            pass


solve()
