n = int(input())
dic = dict()
nodes = list()
ans = 0
for _ in range(n-1):
    raw = list(input().split())
    i = 0
    x = ''
    key = ''
    for char in raw:
        if i > 1:
            if i % 2 == 0:
                if char not in nodes:
                    nodes.append(char)
                key = x + char
            else:
                dic[key] = int(char)
        elif i == 1:
            pass
        elif i == 0:
            if char not in nodes:
                nodes.append(char)
            x = char
        i += 1
cnodes = []
cnodes.append(nodes.pop())
while True:
    mweight = 100
    medge = ''
    onode = ''
    monode = ''
    cweight = ''
    for edge in dic.keys():
        for cnode in cnodes:
            if cnode in edge:
                onode = edge.strip(cnode)
                if onode not in cnodes:
                    cweight = dic[edge]
                    if cweight < mweight:
                        medge = edge
                        mweight = cweight
                        monode = onode
    nodes.remove(monode)
    cnodes.append(monode)
    ans += mweight
    if not nodes:
        break
print(ans)