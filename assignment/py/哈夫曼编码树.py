import heapq

class Node(object):
    _ID = 0
    NodeID:int
    name:str
    sub:list    #List<Node>
    weight:int
    code:str
    strl:list
    def __init__(self, name, weight, l, strl):
        self.NodeID = self._ID
        self.__class__._ID += 1
        self.name = name
        self.sub = l
        self.weight=weight
        self.code = ''
        self.strl = strl
        
    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        elif self.weight == other.weight:
            if self.name != '':
                return self.name < other.name
            else:
                return min(self.strl) < min(other.strl)
        return False
    
    def getName(self):
        if self.name != '':
            return self.name
        else:
            return None
    
    def updateCode(self, i: str) -> None:
        if self.name != '':
            self.code = i + self.code
        for subNode in self.sub:
            if subNode:
                subNode.updateCode(i)
            

class Tree(object):
    tree:dict
    root:Node
    def __init__(self):
        self.tree = dict()
        self.root = None
    
    def add(self, node:Node):
        
        self.tree[node.NodeID] = node   #加入树
        if node.name != '':
            self.tree[node.name] = node
        
        if not self.root:   #尝试转移根节点
            self.root = node

def toTree(l: list) -> Tree:
    myTree = Tree()
    for node in l:
        myTree.add(node)
    while len(l) > 1:
        x, y =  heapq.heappop(l), heapq.heappop(l)
        x.updateCode('0'); y.updateCode('1')
        neoNode = Node('', x.weight + y.weight, [x, y], x.strl + y.strl + [x.getName(), y.getName()])
        myTree.add(neoNode)
        heapq.heappush(l, neoNode)
    node = l[0]
    myTree.root = node
    return myTree


def convert(string: str, myTree: Tree) -> str:
    try:
        _ = int(string)
        root = myTree.root
        res = ''
        i = 0
        while i < len(string):
            char = string[i]
            x = root.sub[int(char)]
            if x:
                root = x
                i += 1
            else:
                res += root.name
                root = myTree.root
        return res + root.name

    except ValueError:
        res = ''
        for char in string:
            res += myTree.tree[char].code
        return res

l = []
for _ in range(int(input())):
    n, w = input().split()
    heapq.heappush(l, Node(n, int(w), [False, False], []))
myTree = toTree(l)
while 1:
    try:
        print(convert(input(), myTree))
    except EOFError:
        break