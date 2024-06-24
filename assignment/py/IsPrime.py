import random

def isPrime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # 将n-1表示为(2^r) * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    def witness(a, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not witness(a, d, n):
            return False
    return True

int = int(input())
print(isPrime(int))