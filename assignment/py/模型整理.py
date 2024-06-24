dic = {'M':1, 'B':1000}
def toFloat(s:str):
    global dic
    c, d = float(s[:-1]), dic[s[-1]]
    c *= d
    return c

n = int(input())
dic2 = {}
for _ in range(n):
    a, b = input().split("-")
    if a not in dic2.keys():
        dic2[a] = []
    dic2[a].append(b)
for key in sorted(dic2.keys()):
    dic2[key].sort(key= lambda x: toFloat(x))
    print(key + ': ' + ", ".join(dic2[key]))
