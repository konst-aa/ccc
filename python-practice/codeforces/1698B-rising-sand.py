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

# solving: https://codeforces.com/contest/1698/problem/B

def solve():
    num_tests = inp()
    ans = []
    for x in range(num_tests):
        num_piles, operations = inlt()
        sizes = inlt()
        if operations == 1:
            ans += [str((num_piles - 1) // 2)]
        else:
            count = 0
            for i in range(1, num_piles - 1):
                count += 1 if sizes[i] > sizes[i-1] + sizes[i+1] else 0
            ans += [str(count)]
    print("\n".join(ans))

solve()
