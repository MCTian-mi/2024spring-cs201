class Node(object):
    _ID = 0
    NodeID:int
    name:str
    sub:list    #List<Node>
    def __init__(self, name, l):
        self.NodeID = self._ID
        self.__class__._ID += 1
        self.sub = []
        self.name = name
        self.sub = l

class Tree(object):
    tree:dict
    root:Node
    def __init__(self):
        self.tree = dict()
        self.root = None
    
    def add(self, node:Node):
        cNodeID = node.NodeID
        
        self.tree[cNodeID] = node   #加入树
        
        if not self.root:   #尝试转移根节点
            self.root = node
            
    def levelOrderFrom(self, node:Node):
        if not node: return []
        
        res, queue = [], [node]
        while queue:
            level_node = []
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_node.append(node.name)
                
                for x in node.sub:
                    if x:
                        queue.append(x)
            res.append(level_node)
            
        return " ".join([" ".join(x) for x in res])

    def levelOrder(self):
         return self.levelOrderFrom(self.root)

def compare(a:str, b:str) -> bool:
    return int(a) < int(b)

def toNode(root:Node, node:Node) -> None:
    if not root:
        return node
    if compare(node.name, root.name):
        root.sub[0] = toNode(root.sub[0], node)
    else:
        root.sub[1] = toNode(root.sub[1], node)
    return root

def toTree(l:list) -> Tree:
    myTree = Tree()
    root = None
    for string in l:
        node = Node(string, [False, False])
        myTree.add(node)
        root = toNode(root, node)
    return myTree

l = list(input().split())
l = list(dict.fromkeys(l))
print(toTree(l).levelOrder())