operatorSet = {'+', '-', '*', '/'}
def isOp(t):
    global operatorSet
    return t in operatorSet
def useable(i):
    global operatorSet
    if i in operatorSet:
        return(i)
    else:
        return((float(i)))
def op(op, i, j):
    if op == '+':
        return i + j
    elif op == '-':
        return i - j
    elif op == '*':
        return i * j
    else:
        return i / j

l = list(map(useable, input().split()))
stack = []
i = -1
while 1:
    try:
        x = l[i]
        if isOp(x):
            stack.append(op(x, stack[-1], stack[-2]))
            stack.pop(-2)
            stack.pop(-2)
        else:
            stack.append(x)
        i -= 1
    except IndexError:
        print("%.6f\n"%stack[-1])
        break