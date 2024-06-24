t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    indegree = [0] * n
    fromnode = {i : [] for i in range(n)}
    for _ in range(m):
        sp, tp = map(int, input().split())
        sp, tp = sp - 1, tp - 1
        fromnode[sp].append(tp)
        indegree[tp] += 1
    visited = 0
    tovisit = []
    for i in range(n):
        if indegree[i] == 0:
            tovisit.append(i)
    while tovisit:
        cnode = tovisit.pop()
        visited += 1
        for node in fromnode[cnode]:
            indegree[node] -= 1
            if indegree[node] == 0:
                tovisit.append(node)
    print(['Yes', 'No'][visited == n])