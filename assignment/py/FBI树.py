class Node(object):
    _ID = 0
    NodeID:int
    name:str
    sub:list    #List<Node>
    def __init__(self, name, sub):
        self.NodeID = self._ID
        self.__class__._ID += 1
        self.name = name
        self.sub = sub
    

class Tree(object):
    tree:dict
    root:Node
    def __init__(self):
        self.tree = dict()
        self.root = None
    
    def add(self, node:Node):
        cNodeID, cSubNodes = node.info()
        
        self.tree[cNodeID] = node   #加入树
        
        if not self.root:   #尝试转移根节点
            self.root = node

    def postOrderFrom(self, node:Node):  # 后序遍历
        if not node: return ''
        return  "".join([self.postOrderFrom(x) for x in node.sub]) + node.name
    def postOrder(self):
        return self.postOrderFrom(self.root)
     
     
def check(string):
    if '0' in string:
        if '1' in string:
            return 'F'
        else:
            return 'B'
    else:
        return 'I'
           
def toNode(string) -> Node:
    x = len(string)
    if x > 1:
        return Node(check(string), [toNode(string[:x//2]), toNode(string[x//2:])])
    else:
        return Node(check(string), [False, False])

def toTree(string) -> Tree:
    myTree = Tree()
    myTree.root = toNode(string)
    return myTree

n = int(input())
string = input()
myTree = toTree(string)
print(myTree.postOrder())