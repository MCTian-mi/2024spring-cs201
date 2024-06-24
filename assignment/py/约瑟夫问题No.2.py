while 1:
    n, p, m = map(int, input().split())
    if (n, p, m) == (0, 0, 0):
        break
    l = list(range(p, n + 1)) + list(range(1, p))
    ans = []
    while len(l) > 0:
        length = len(l)
        x = m % length - 1
        ans.append(l[x])
        if x != -1:
            l = l[x+1:] + l[0:x]
        else:
            l.pop(-1)
    print(",".join([str(x) for x in ans]))