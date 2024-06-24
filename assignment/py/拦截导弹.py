n = int(input())
l = [int(x) for x in input().split()]
dp = [[0,999999999]]
for i in range(n):
    temp = l[i]
    for j in range(len(dp)):
        if temp <= dp[j][1]:
            dp += [[dp[j][0] + 1, temp]]
ans = max([x[0] for x in dp])
print(ans)