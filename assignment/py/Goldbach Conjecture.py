from math import ceil, sqrt

def isprime(n:int):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

Sum = int(input())
for i in range(2, Sum//2 + 1):
    j = Sum - i
    if (isprime(i) and isprime(j)):
        print(i, j)
        break