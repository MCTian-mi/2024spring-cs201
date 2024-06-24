n = int(input())
l = list(map(int, input().split()))
lBoth = []
for i in range(n):
    lBoth.append([i, l[i]])
lBoth.sort(key=lambda x: x[1])
lIndex = [x[0] for x in lBoth]
sumy = 0
j = n - 1
for i in range(n):
    sumy += j * lBoth[i][1]
    j -= 1
print(" ".join([str(x+1) for x in lIndex]) + '\n' + "%.2f"%(sumy/n))