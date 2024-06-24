import bisect
import itertools
count = 0
n = int(input())
A, B, C, D = zip(*[map(int, input().split()) for _ in range(n)])
lf = list(map(sum, itertools.product(A, B)))
lf.sort()
for x in map(sum, itertools.product(C, D)):
    count += bisect.bisect_right(lf, -x) - bisect.bisect_left(lf, -x)
print(count)