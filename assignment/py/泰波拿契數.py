n = int(input())
l = [0, 1, 1]
if n <= 2:
    print(l[n])
else:
    for i in range(n-2):
        l.append(sum(l))
        l.pop(0)
    print(l[2])