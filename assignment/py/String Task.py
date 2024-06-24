original = input().lower()
ans = ""
notallowed = "aeiouy"
for char in original:
    if not char in notallowed:
        ans += "." + char
print(ans)