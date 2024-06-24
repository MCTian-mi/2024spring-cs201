def check(word : str):
    checklist = "hello"
    i = 0
    for char in word:
        if char == checklist[i]:
            i += 1
            if i == 5:
                return("YES")
    return("NO")
print(check(input()))