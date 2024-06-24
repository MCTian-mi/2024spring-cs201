n = int(input())
l = [float('inf')] + [int(input()) for _ in range(n)] + [0]
rmin = dict()
lmax = dict()
stackmin = [0]
stackmax = [n + 1]
for i in range(1, n + 2):
    while len(stackmin) > 1 and l[stackmin[-1]] >= l[i]:
        rmin[stackmin.pop()] = i
    stackmin.append(i)
for i in range(n, -1, -1):
    while len(stackmax) > 1 and l[stackmax[-1]] <= l[i]:
        lmax[stackmax.pop()] = i
    stackmax.append(i)
ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, rmin[i]):
        if i > lmax[j]:
            ans = max(ans, j - i + 1)
print(ans)