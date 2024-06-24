s = set()
x, y = map(int, input().split())
for i in range(y):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        s.add(j)
print(x + 1 - len(s))