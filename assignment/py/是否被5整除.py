x = input()
c = 0
ans = ''
for i in x:
    c *= 2
    c += int(i)
    if c % 5 == 0:
        ans += '1'
    else:
        ans += '0'
print(ans)