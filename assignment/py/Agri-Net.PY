from heapq import *

while True:
    try:
        n = int(input())
        temp = []
        l = [list(map(int, input().split())) for _ in range(n)]
        visited = [0]
        unvisited = list(range(1, n))
        ans = 0
        ways = []
        for onode in unvisited:
            heappush(ways, (l[0][onode], 0, onode))
        while unvisited:
            way = heappop(ways)
            weight, this, other = way
            if other in visited:
                continue
            ans += weight
            visited.append(other)
            unvisited.remove(other)
            for onode in unvisited:
                heappush(ways, (l[other][onode], other, onode))
        print(ans)
    except EOFError:
        break