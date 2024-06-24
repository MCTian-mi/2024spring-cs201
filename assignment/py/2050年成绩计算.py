from math import sqrt

N = 10000
primeList = []
pOn = [False] * 2 + [True] * (N-1)
p = 2
while p <= N:
    if pOn[p]:
        primeList.append(p)
    for i in primeList:
        x = p * i 
        if  x > N:
            break
        pOn[x] = False
        if p % i == 0:
            break
    p += 1

def istprime(n:int):
    x = sqrt(n)
    return x.is_integer() and pOn[int(x)]

yes = "YES"
no = "NO"

m, _ = map(int, input().split())
for i in range(m):
    vs = list(map(int, input().split()))
    v = 0
    for i in vs:
        if istprime(i):
            v += i
    if v == 0:
        print(0)
    else:
        print(format(v/len(vs),".2f"))