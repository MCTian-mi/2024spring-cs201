m, n = map(int, input().split())
l = list(map(int, input().split()))
i = 0
mem = []

def add(l, string):
    global m
    if len(l) == m:
        l.pop(0)
    l.append(string)

def check(l, string):
    global i
    if string in l:
        return
    else:
        add(l, string)
        i += 1
        return

i = 0
for string in l:
    check(mem, string)
print(i)