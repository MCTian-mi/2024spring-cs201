from heapq import *

move_offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]

inf = float('inf')
m, n, p = map(int, input().split())
l = [list(map(lambda x: inf if x == '#' else int(x), input().split())) for _ in range(m)]


def bfs(x0, y0, xt, yt):
    global l, m, n, move_offset, inf
    distance = [[inf] * n for _ in range(m)]
    if l[y0][x0] == inf or l[yt][xt] == inf: return 'NO'
    distance[y0][x0] = 0
    front = [(0, x0, y0)]
    while front:
        d, x, y = heappop(front)
        if (x, y) == (xt, yt):
            return d
        h = l[y][x]
        for movement in move_offset:
            i, j = movement
            xn, yn = x + i, y + j
            node = (xn, yn)
            
            if 0 <= xn < n and 0 <= yn < m and l[yn][xn] != inf:
                dn = abs(l[yn][xn] - h) + d
                if distance[yn][xn] > dn:
                    distance[yn][xn] = dn
                    heappush(front, (dn, xn, yn))
    return 'NO'

for _ in range(p):
    y0, x0, yt, xt = map(int, input().split())
    print(bfs(x0, y0, xt, yt))