def check(str):
    x = int(str)
    if x == -1:
        return False
    else:
        return x
n = int(input())
tree = [[]] + [list(map(check, input().split())) for _ in range(n)]

def s(node, ans = [], level = 0):
    global tree
    try:
        ans[level]
    except IndexError:
        ans.append(-1)
    ans[level] = str(node)
    if tree[node][0]:
        s(tree[node][0], ans, level + 1)
    if tree[node][1]:
        s(tree[node][1], ans, level + 1)
    return ans

print(' '.join(s(1)))