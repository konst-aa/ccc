n = int(input())
camels = {}
for _ in range(n):
    a, b = map(int, input().split())
    camels[a] = a + b

for c, t in camels.items():
    if t in camels and camels[t] == c:
        print("YES")
        exit(0)

print("NO")
