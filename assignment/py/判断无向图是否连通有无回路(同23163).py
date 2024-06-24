n, m = map(int, input().split())
l = [[False] * n for _ in range(n)]
true = [[True] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    l[a][b] = l[b][a] = True

connected = 'yes'
loop = 'no'
black = []
grey = []
q = [0]
while q:
    c = q.pop()
    if c in black:
        continue
    grey.append(c)
    for i in range(n):
        if l[c][i]:
            if i in black:
                continue
            if i in grey and i:
                loop = 'yes'
                continue
            q.append(i)
            grey.append(i)
    black.append(c)
    f = c
if len(black) != n:
    connected = 'no'
print('connected:{}\nloop:{}'.format(connected, loop))
