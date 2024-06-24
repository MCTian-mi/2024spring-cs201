from __future__ import annotations

class Node:
    _ID = 0
    NodeID:int
    name:str
    sub:list
    parent:Node
    
    def __init__(self, name, sub, parent=None):
        self.NodeID = Node._ID
        Node._ID += 1
        self.name = name
        self.sub = sub
        self.parent = parent
        
class BiTree(dict):
    root:Node
    def __init__(self):
        self.parent = dict()
        self.root = None
    
    def findParent(self, t):
        if t not in self.parent:
            return None
        return self.parent[t]
    
    def getOrCreate(self, nodename):
        if nodename == "-1":
            return False
        if nodename not in self:
            self[nodename] = Node(nodename, [False, False])
        return self[nodename]
        
    def add(self, t, l, r):
        if t not in self:
            neonode = Node(t, [self.getOrCreate(l), self.getOrCreate(r)])
            self[t] = neonode
        else:
            neonode = self[t]
            neonode.sub = [self.getOrCreate(l), self.getOrCreate(r)]
        if not self.root:
            self.root = neonode
        if l != "-1":
            self.parent[l] = neonode
        if r != "-1":
            self.parent[r] = neonode
            
    def initTree(self):
        for nodename in self:
            if nodename == '0':
                continue
            node:Node = self[nodename]
            node.parent = self.parent[nodename]
    
    def exchange(self, i, j):
        inode:Node = self[i]
        jnode:Node = self[j]
        if inode.parent == jnode.parent:
            inode.parent.sub.reverse()
        else:
            for i in range(2):
                if inode.parent.sub[i] == inode:
                    inode.parent.sub[i] = jnode
                if jnode.parent.sub[i] == jnode:
                    jnode.parent.sub[i] = inode
            inode.parent, jnode.parent = jnode.parent, inode.parent
        
    def _findleftest(self, node:Node):
        if node.sub[0]:
            return self._findleftest(node.sub[0])
        else:
            return node.name
    
    def findleftest(self, i):
        return self._findleftest(self[i])

for _ in range(int(input())):
    n, m = map(int, input().split())
    myTree = BiTree()
    for __ in range(n):
        myTree.add(*input().split())
    myTree.initTree()
    for ___ in range(m):
        codein = list(input().split())
        if codein[0] == "1":
            myTree.exchange(codein[1], codein[2])
        else:
            print(myTree.findleftest(codein[1]))