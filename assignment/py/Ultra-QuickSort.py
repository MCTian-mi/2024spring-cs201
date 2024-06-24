count = 0
def merge(la, lb):
    global count
    i = j = 0; lc = []
    while i < len(la) and j < len(lb):
        if lb[j] < la[i]:
            lc.append(lb[j])
            count += len(la) - i
            j += 1
        else:
            lc.append(la[i])
            i += 1
    lc += la[i:] + lb[j:]
    return lc
def ultraQuickSort(l, lIndex, rIndex):
    if rIndex - lIndex <= 1:
        return
    mIndex = (lIndex + rIndex) // 2
    ultraQuickSort(l, lIndex, mIndex)
    ultraQuickSort(l, mIndex, rIndex)
    l[lIndex:rIndex] = merge(l[lIndex:mIndex], l[mIndex:rIndex])

while 1:
    x = int(input())
    if x == 0: break
    count = 0
    l = [int(input()) for _ in range(x)]
    ultraQuickSort(l, 0, x)
    print(count)