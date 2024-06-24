n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
if k == 0 and 1 not in l:
    print(1)
elif k == 0:
    print(-1)
elif k == n:
    print(l[-1])
else:
    try:
        if l[k] > l[k-1]:
            print(l[k-1])
        else:
            print(-1)
    except IndexError:
        print(-1)
