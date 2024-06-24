from collections import deque


class Node(object):
    NodeID:int
    pNodeID:int
    lNodeID:int
    rNodeID:int
    def __init__(self, NodeID, lNodeID:int, rNodeID:int, pNodeID:int=-1):
        self.NodeID = NodeID
        self.lNodeID = lNodeID
        self.rNodeID = rNodeID
        self.pNodeID = pNodeID
    def __str__(self):  #Debug
        return "🌿{} p:{}, l:{}, r:{}".format(self.NodeID, self.pNodeID, self.lNodeID, self.rNodeID)
    def info(self):
        return (self.NodeID, self.lNodeID, self.rNodeID)
    
class BiTree(object):
    tree:dict
    root:Node
    def __init__(self):
        self.tree = dict()
        self.root = None
    
    def add(self, node:Node):
        cNodeID, cNodeLID, cNodeRID = node.info()
        
        self.tree[cNodeID] = node   #加入树
        
        if not self.root:   #尝试转移根节点
            self.root = node
        elif self.root.NodeID == cNodeLID or self.root.NodeID == cNodeRID:
            self.root = node
            
        for nodes in self.tree.values():    #尝试添加父节点
            aNodeID, aNodeLID, aNodeRID = nodes.info()
            if cNodeID == aNodeLID or cNodeID == aNodeRID:  #是子节点
                node.pNodeID = aNodeID
    def get(self, nodeID:int):
        if nodeID == -1:
            return False
        else:
            return self.tree[nodeID]
    def getDepth(self, node:Node):
        if node:
            return(1 + max(self.getDepth(self.get(node.lNodeID)), self.getDepth(self.get(node.rNodeID))))
        else:
            return 0  
    def getTreeDep(self):
        return self.getDepth(self.root)

n = int(input())
myBiTree = BiTree()
for i in range(n):
    l, r = map(int, input().split())
    myBiTree.add(Node(i + 1, l, r))
print(myBiTree)