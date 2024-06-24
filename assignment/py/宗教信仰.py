class DisjointSet(object):
    father_dict:dict
    def __init__(self, l):
        self.father_dict = {}
        for x in l:
            self.father_dict[x] = x
    def find(self, x):
        if self.father_dict[x] == x:
            return x
        else:
            self.father_dict[x] = self.find(self.father_dict[x])
            return self.father_dict[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.father_dict[py] = px
            return 'No'
        else:
            return 'Yes'
    def getUnions(self):
        return sorted(list(set(self.father_dict.values())))

i = 0
while 1:
    try:
        n, m = map(int, input().split())
        if n == m == 0: raise EOFError
        i += 1
        ds = DisjointSet(list(range(1, n + 1)))
        for _ in range(m):
            a, b = map(int, input().split())
            if a > b:
                a, b = b, a
            ds.union(a, b)
        rgs = set(ds.find(x) for x in range(1, n + 1))
        print("Case {}: {}".format(i, len(rgs)))
        print(ds.getUnions())
    except EOFError:
        break