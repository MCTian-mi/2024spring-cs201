class Node(object):
    _ID = 0
    NodeID:int
    name:str
    value:int
    height:int
    sub:list
    
    def __init__(self, name, l):
        self.NodeID = self._ID
        self.__class__._ID += 1
        self.name = name
        self.value = int(name)
        self.sub = l
        self.height = 0
    def getHeight(self):
        x = max([-1] + [subNode.getHeight() for subNode in self.sub if subNode]) + 1
        self.height = x
        return x
    def getBF(self):
        left = right = -1
        if self.sub[0]:
            left = self.sub[0].getHeight()
        if self.sub[1]:
            right = self.sub[1].getHeight()
        return left - right
    

class Tree(object):
    tree:dict
    root:Node
    def __init__(self):
        self.tree = dict()
        self.root = None
    def insert(self, node) -> None:
        if self.root == None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)
    def _insert(self, root, node:Node) -> None:
        if not root:
            return node
        else:
            if node.value < root.value:
                root.sub[0] = self._insert(root.sub[0], node)
            else:
                root.sub[1] = self._insert(root.sub[1], node)
            
            bf = root.getBF()
            if bf == 2:
                if node.value > root.sub[0].value:
                   root.sub[0] = self._rotate(root.sub[0], True)
                return self._rotate(root, False)
            elif bf == -2:
                if node.value < root.sub[1].value:
                    root.sub[1] = self._rotate(root.sub[1], False)
                return self._rotate(root, True)
            return root
    def _rotate(self, node:Node, lRotate:bool):
        bNode = node.sub[lRotate]
        dNode = bNode.sub[not lRotate]
        if dNode:
            dNode.pNode = node
        node.sub[lRotate] = dNode
        bNode.sub[not lRotate] = node
        return bNode
        
    def preOrderFrom(self, node:Node):
        return node.name + " " + "".join([self.preOrderFrom(x) for x in node.sub if x])
    def preOrder(self):
        return self.preOrderFrom(self.root)
            

myTree = Tree()
_ = input()
for x in input().split():
    myTree.insert(Node(x, [False, False]))
print(myTree.preOrder().rstrip())
