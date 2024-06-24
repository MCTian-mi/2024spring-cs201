a, b, c =map(int, input().split())
unvisited = [[True] * (a + 1) for _ in range(b + 1)]

def bfs(l, depth = 0):
    global a, b, c, unvisited
    nextl = []
    for traceablepos in l:
        x, y, string = traceablepos
        if 0 <= x <= a and 0 <= y <= b and unvisited[y][x]:
            if x == c or y == c:
                return str(depth) + string
            unvisited[y][x] = False
            if x < a:
                nextl.append((a, y, string + '\nFILL(1)'))
            if y < b:
                nextl.append((x, b, string + '\nFILL(2)'))
            if x > 0:
                nextl.append((0, y, string + '\nDROP(1)'))
                if y < b:
                    remain = y + x - b
                    if remain >= 0:
                        nextl.append((remain, b, string + '\nPOUR(1,2)'))
                    else:
                        nextl.append((0, x + y, string + '\nPOUR(1,2)'))
            if y > 0:
                nextl.append((x, 0, string + '\nDROP(2)'))
                if x < a:
                    remain = x + y - a
                    if remain >= 0:
                        nextl.append((a, remain, string + '\nPOUR(2,1)'))
                    else:
                        nextl.append((x + y, 0, string + '\nPOUR(2,1)'))
    if not nextl:
        return 'impossible'
    return bfs(nextl, depth + 1)

print(bfs([(0, 0, '')]))