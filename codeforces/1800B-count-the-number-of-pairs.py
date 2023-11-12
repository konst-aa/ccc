cases = int(input())

for _ in range(cases):
    _, ops = map(int, input().split())
    inp = input()
    count = 0
    dct = {}

    for c in inp:
        if c.lower() not in dct:
            dct[c.lower()] = []
        cl = dct[c.lower()]

        if len(cl) == 0:
            cl.append(c)
        elif (cl[-1].islower() and c.isupper()) or (cl[-1].isupper() and c.islower()):
            cl.pop()
            count += 1
        else:
            cl.append(c)

    
    
    op_count = 0
    for b in dct.values():
        op_count += len(b) // 2

    print(count + min(ops, op_count))
