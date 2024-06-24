from math import sqrt

N = 1000000
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

_ = int(input())
for x in list(map(int, input().split())):
    print([no, yes][istprime(x)])