from heapq import *
class Road:
    start:int
    destination:int
    length:int
    cost:int
    def __init__(self, s, d, l, t):
        self.start = s
        self.destination = d
        self.length = l
        self.cost = t
    def __lt__(self, other):
        return self.length < other.length
    def __eq__(self, other):
        return self.length == other.length

k = int(input())
n = int(input())
r = int(input())
roads = {city : [] for city in range(1, n + 1)}
for _ in range(r):
    s, d, l, t = map(int, input().split())
    newRoad = Road(s, d, l, t)
    roads[s].append(newRoad)

def work():
    ways = [(0, 1, k, [])]
    while ways:
        info = heappop(ways)
        distance, currentcity, remain, passedcities = info
        if currentcity == n:
            print(distance)
            return
        for roadfc in roads[currentcity]:
            if roadfc.destination in passedcities or roadfc.cost > remain:
                continue
            else:
                heappush(ways, (distance + roadfc.length, roadfc.destination,
                                remain - roadfc.cost, passedcities + [currentcity]))
    print(-1)
    return 
work()