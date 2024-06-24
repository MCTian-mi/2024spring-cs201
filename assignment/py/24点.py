n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    sety = {+a+b+c+d,+a+b+c-d,+a+b-c+d,+a-b+c+d,-a+b+c+d,+a+b-c-d,+a-b-c+d,+a-b+c-d}
    if -24 not in sety and 24 not in sety:
        print("NO")
    else:
        print("YES")