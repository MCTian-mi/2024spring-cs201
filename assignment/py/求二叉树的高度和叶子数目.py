class treeNode(object):
    leftSubNodeID:int
    rightSubNodeID:int
    nodeID:int
    level:int = 0
    isLeafNode:bool = False
    def __init__(self, id, left, right):
        self.leftSubNodeID = left
        self.rightSubNodeID = right
        self.nodeID = id
        if left == -1 == right:
            self.isLeafNode = True
            
    def getLeftSubeNodeID(self):
        return self.leftSubNodeID
    def getRightSubNodeID(self):
        return self.rightSubNodeID
    def getLevel(self):
        return self.level
    def setLevel(self, int):
        self.level = int

class biTree(object):
    nodeDic:dict
    depth:int = 0
    leaf:int = 0
    def __init__(self):
        self.nodeDic = dict()
    def add(self, key, node):
        self.nodeDic[key] = node
    def get(self, key):
        if key == -1:
            return False
        else:
            return self.nodeDic[key]
    def init(self):
        for treeNodeID, treeNode in self.nodeDic.items():
            if not treeNode.isLeafNode:
                self.depth = max(self.depth, self.getNodeLevel(treeNodeID))
            else:
                self.leaf += 1
    def getNodeLevel(self, nodeID):
            currentNode = self.get(nodeID)
            if currentNode:
                if currentNode.isLeafNode:
                    return 0
                else:
                    if currentNode.level == 0:
                        currentNode.setLevel(1 + max(self.getNodeLevel(currentNode.getLeftSubeNodeID())
                                                     , self.getNodeLevel(currentNode.getRightSubNodeID())))
                    return currentNode.level
            return -1
        
n = int(input())
myBiTree = biTree()
for i in range(n):
    l, r = map(int, input().split())
    myBiTree.add(i, treeNode(i, l, r))
myBiTree.init()
print(myBiTree.depth, myBiTree.leaf)