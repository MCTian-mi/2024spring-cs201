def bfs(x:int, l:list=[1]):
    for y in l:
        if y % x == 0:
            return y
    l2 = []
    for y in l:
        l2.append(10*y + 0)
        l2.append(10*y + 1)
    return bfs(x, l2)

while True:
    x = int(input())
    if x != 0:
        print(bfs(x))
    else:
        break