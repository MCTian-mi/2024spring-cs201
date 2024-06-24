from heapq import *

V = [10, 40]

# class edge:
#     x0:int
#     y0:int
#     xt:int
#     yt:int
    
#     def __init__(self, x0, y0, xt, yt):
#         self.x0 = x0
#         self.y0 = y0
#         self.xt = xt
#         self.yt = yt
        
class way:
    node:tuple
    time:float
    passed:list
    
    def __init__(self, node0, time = 0, passed = list()):
        self.node = node0
        self.time = time
        self.passed = passed
    
    def parse(self, onode, is_by_sub):
        ox, oy = onode
        v = V[is_by_sub]
        otime = self.time + ((ox - self.node[0])**2 + (oy - self.node[1])**2)**.5 / v
        return way(onode, otime, self.passed + [self.node])
    def __lt__(self, other):
        return self.time < other.time
        

X0, Y0, XT, YT = map(int, input().split())
TNODE = (XT, YT)
edges = {}
nodes = [(X0, Y0), (XT, YT)]
while 1:
    try:
        l = list(map(int, input().split()))
        fnode = None
        for i in range(0, len(l), 2):
            x = l[i]
            y = l[i + 1]
            if x == -1: break
            cnode = (x, y)
            if cnode not in nodes:
                nodes.append(cnode)
            if fnode:
                try:
                    edges[fnode]
                except:
                    edges[fnode] = []
                edges[fnode].append(cnode)
            fnode = cnode
    except:
        break
ways = [way((X0, Y0))]
while ways:
    cway = ways.pop()
    cnode = cway.node
    if cnode == TNODE:
        print(cway.time)
        break
    try:
        for onode in edges[cnode]:
            if onode not in cway.passed:
                heappush(ways, cway.parse(onode, True))
    except KeyError:
        pass
    for onode in nodes:
        if onode != cnode and onode not in cway.passed:
            heappush(ways, cway.parse(onode, False))