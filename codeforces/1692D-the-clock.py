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


# solving: https://codeforces.com/problemset/problem/1692/D


def next_incr(pos, increment):
    pos = (pos[0] + increment[0], pos[1] + increment[1])
    return ((pos[0] + pos[1] // 60) % 24, pos[1] % 60)


def solve():
    num_tests = inp()
    palindrome_cycles = set(
        (int(x), int(x[::-1]))
        for x in [str(a) + str(b) for a in range(3) for b in range(10)]
    )  # as long as the incrementing doesn't get invalid numbers, all sorts of
    # invalid timestamps that could be generated here idc about.
    for x in range(num_tests):
        timestamp, mins = input().split()
        cycle_length = int(mins)
        increment = (cycle_length // 60, cycle_length % 60)
        cycle_start = tuple(map(int, timestamp.split(":")))
        cur_cycle = next_incr(cycle_start, increment)
        acc = set([cycle_start])
        while cur_cycle not in acc:
            acc.add(cur_cycle)
            cur_cycle = next_incr(cur_cycle, increment)
        print(len(palindrome_cycles.intersection(acc)))


solve()
