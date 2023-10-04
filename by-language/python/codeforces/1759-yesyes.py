cases = int(input())

for i in range(cases):
    case = input()
    cycle = "Yes"
    cyci = cycle.find(case[0])
    b = cyci == -1
    for ch in case:
        if not b and cycle[cyci] != ch:
            b = True
        cyci += 1
        if cyci > 2:
            cyci = 0
    print("YES" if not b else "NO")
