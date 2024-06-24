class treeNode(object):
    leftSubNodeID:int
    rightSubNodeID:int
    nodeID:int
    
    def __init__(self, id, left, right):
        self.leftSubNodeID = left
        self.rightSubNodeID = right
        self.nodeID = id
    def getLeftSubeNodeID(self):
        return self.leftSubNodeID
    def getRightSubNodeID(self):
        return self.rightSubNodeID

class biTree(object):
    nodeDic:dict
    
    def __init__(self):
        self.nodeDic = dict()
    def add(self, key, node):
        self.nodeDic[key] = node
    def get(self, key):
        if key == -1:
            return False
        else:
            return self.nodeDic[key]
    def getTreeDep(self, nodeID=1):
        currentNode = self.get(nodeID)
        if currentNode:
            return(1 + max(self.getTreeDep(currentNode.getLeftSubeNodeID()), self.getTreeDep(currentNode.getRightSubNodeID())))
        else:
            return 0    
    
n = int(input())
myBiTree = biTree()
for i in range(n):
    l, r = map(int, input().split())
    myBiTree.add(i + 1, treeNode(i + 1, l, r))
print(myBiTree.getTreeDep())