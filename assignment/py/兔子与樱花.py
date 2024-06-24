from heapq import *

inf = float('inf')

p = int(input())
distance = dict()
l = [input() for _ in range(p)]
for i in l:
    distance[i] = dict()
    for j in l:
        distance[i][j] = inf

q = int(input())
for _ in range(q):
    i, j, dis = input().split()
    distance[i][j] = distance[j][i] = int(dis)

r = int(input())

def to(traceablepos, target):
    global l, distance
    dis, pos, info = traceablepos
    return (dis + distance[pos][target], target, info + '->({})->{}'.format(distance[pos][target], target))

def bfs(origin, terminal):
    global distance
    
    nearest = dict()
    for i in l:
        nearest[i] = inf
            
    ways = [(0, origin, origin)]
    
    while ways:
        traceablepos = heappop(ways)
        dis, pos, info = traceablepos
        if pos == terminal:
            return info
        for target in l:
            if distance[pos][target] != inf and nearest[target] > dis + distance[pos][target]:
                nearest[target] = dis + distance[pos][target]
                heappush(ways, to(traceablepos, target))
    raise FileNotFoundError

for _ in range(r):
    print(bfs(*input().split()))