from multiprocessing import Process
for _ in range(int(input())):
    n, x = map(int, input().split())
    lIndex = -1
    rIndex = -1
    sum = 0
    listA = list(map(int, input().split()))
    length = len(listA)
    for i in range(length):
        rmdr = listA[i] % x
        if rmdr != 0:
            if lIndex == -1:
                lIndex = i
                rIndex = i
            rIndex = max(rIndex, i)
        sum += rmdr
    if sum % x != 0:
        print(n)
    elif lIndex == -1:
        print(-1)
    else:
        print(max(length-lIndex-1, rIndex))