# Implement the following function
def directions(fr, to):
    path1 = "ADCB" * 2
    path2 = "ABCD" * 2
    dirs = []
    for path in (path1, path2):
        dr = []
        i = path.index(fr) + 1
        while path[i] != to:
            dr += [path[i]]
            i += 1
        dirs += [dr + [to]]
    return dirs


def evacuate(n, k, order, duration, sfx):
    hist = []
    ports = {}
    running = 0
    for portal, time in zip(order, duration):
        running += time
        hist += [running]
        ports[running] = portal
    civilians = []
    for (fr, to, time) in sfx:
        time = int(time)
        res = []
        for path in directions(fr, to):
            b = False
            start_index = len(hist)
            for i in range(len(hist)):
                if not b and time < hist[i]:
                    start_index = i
                    b = True
            b = False
            past = time
            for i in range(start_index, len(hist)):
                # print("wha?")
                if not b and ports[hist[i]] == path[0]:
                    path.pop(0)
                if not path:
                    b = True
                if not b:
                    past = hist[i]
            res += [-1 if past == hist[-1] else past - time]
        civilians += [-1 if res == [-1, -1] else min(filter(lambda i: i != -1, res))]
    return civilians


# print(evacuate(1000, 1000, ["A"] * 1000 + ["D"], [1] * 1000000001, [["A", "D", 0]] * 1000))
tests = int(input().strip())  # Number of test cases
for test in range(tests):
    line = input().strip().split(" ")
    n = int(line[0])
    k = int(line[1])
    order = input().strip().split(" ")  # List of which portals turn on in order
    duration = input().strip().split(" ")  # List of times when portals are on for
    duration = [int(x) for x in duration]
    sfx = []  # List of triplets (start_portal, destination_portal, arrival_time)
    for _ in range(k):
        sfx.append(input().strip().split(" "))
    ret_arr = evacuate(n, k, order, duration, sfx)
    ret_arr = [str(x) for x in ret_arr]
    print("\n".join(ret_arr))
