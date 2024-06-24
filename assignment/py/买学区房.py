def findMedian(l):
    leng = len(l)
    ls = sorted(l)
    if  leng & 1:
        return ls[(leng-1)//2]
    else:
        return (ls[leng//2] + ls[(leng)//2-1])/2

n = int(input())
pairs = [i[1:-1] for i in input().split()]
distanceOrRatios = [sum(map(int,i.split(','))) for i in pairs]
values = list(map(int, input().split()))
for i in range(n):
    distanceOrRatios[i] /= values[i]
medianRatio, medianValue = findMedian(distanceOrRatios), findMedian(values)
ans = 0
for i in range(n):
    if distanceOrRatios[i] > medianRatio and values[i] < medianValue:
        ans += 1
print(ans)