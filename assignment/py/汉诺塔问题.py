def d(i,a,b):
    return str(i) + ":" + a + "->" + b

def countMoves(n, a, b, c):
    if n == 3:
        return[d(1,a,c), d(2,a,b), d(1,c,b), d(3,a,c), d(1,b,a), d(2,b,c), d(1,a,c)]
    else:
        return countMoves(n-1, a, c, b) + [d(n,a,c)] + countMoves(n-1, b, a, c)

n, a, b, c = input().split()
n = int(n)
print("\n".join(countMoves(n,a,b,c)))