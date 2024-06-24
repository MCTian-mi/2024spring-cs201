directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
l = [list(input()) for _ in range(10)]
unchecked = [[True] * 10 for _ in range(10)]
ans = 0

def dfs(j, i):
    global l, unchecked, ans
    if 0 <= i < 10 and 0 <= j < 10 and unchecked[j][i]:
        unchecked[j][i] = False
        if l[j][i] == '-':
            return 0
        else:
            for direction in directions:
                y, x = direction
                dfs(j + y, i + x)
        return 1
    return 0

for j in range(10):
    for i in range(10):
        if unchecked[j][i]:
            ans += dfs(j, i)

print(ans)