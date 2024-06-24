from heapq import *

for _ in range(int(input())):
    lb = []
    ls = []
    count = 0
    shouldprint = True
    ans = []
    for x in map(int, input().split()):
        if not lb or -lb[0] >= x:
            heappush(lb, -x)
        else:
            heappush(ls, x)
        if len(ls) > len(lb):
            heappush(lb, - heappop(ls))
        if len(lb) > len(ls) + 1:
            heappush(ls, - heappop(lb))
        if shouldprint:
            ans.append(str(-lb[0]))
        shouldprint = not shouldprint
    print(str(len(ans)) + '\n' +' '.join(ans))