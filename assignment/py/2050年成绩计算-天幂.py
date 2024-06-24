from multiprocessing import Process, Value, Array
from math import sqrt

def do(p, s):
    global N
    for i in range(p * 2, N, p):
        s[i] = False

N = 10005    
s = Array('b', [True] * N)

if __name__ == "__main__":
    p = 2
    while p * p <= N:
        if s[p]:
            process = Process(target=do, args=(p, s))
            process.start()
        p += 1
    m, n = [int(i) for i in input().split()]
    for i in range(m):
        x = [int(i) for i in input().split()]
        sum = 0
        for num in x:
            root = int(sqrt(num))
            if num > 3 and s[root] and num == root * root:
                sum += num
        sum /= len(x)
        if sum == 0:
                print(0)
        else:
            print('%.2f' % sum)