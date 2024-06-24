operatorSet = {'+', '-', '*', '/', '(', ')'}
operatorWeight = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1, ')': -1}
def isOp(t):
    global operatorSet
    return t in operatorSet
def op(op, i, j):
    if op == '+':
        return i + j
    elif op == '-':
        return i - j
    elif op == '*':
        return i * j
    else:
        return i / j
def useable(string):
    val = []
    number = ""
    global operatorSet
    for x in string:
        if x in operatorSet:
            if number:
                val.append(number)
            val.append(x)
            number = ""
        else:
            number += x
    if number:
        val.append(number)
    return val

for _ in range(int(input())):
    ans = []
    stack = []
    n = 0
    l = ["("] + useable(input()) +[")"]
    while 1:
        try:
            x = l[n]
            if isOp(x):
                if x == '(':
                    stack.append(x)
                elif x == ')':
                     while 1:
                        y = stack[-1]
                        if y != '(':
                            ans.append(y)
                            stack.pop()
                        else:
                            stack.pop()
                            break
                else:
                    
                    while operatorWeight[stack[-1]] >= operatorWeight[x]:
                        ans.append(stack[-1])
                        stack.pop()
                    stack.append(x)
            else:
                ans.append(x)
            n += 1
        except IndexError:
            stack.reverse()
            print(' '.join(ans + stack))
            break