indent = "|     "
enter = "\n"

def getPos(node):
    name = node.name
    if name.startswith('d'):
        return str(node.NodeID)
    else:
        return name

class Node(object):
    _ID = 0
    NodeID:int
    pNodeID:int
    name:str
    sub:list    #List<Node>
    depth:int
    def __init__(self, name, l, pNodeID= -1, depth:int=0):
        self.NodeID = self._ID
        self.__class__._ID += 1
        self.pNodeID = pNodeID
        self.sub = []
        self.name = name
        self.depth = depth
        for node in l:
            self.sub.append(node)
    def info(self):
        return (self.NodeID, self.sub)
    def toString(self, depth:int=-1):
        if self.name.startswith('d') or self.name == "ROOT":
            self.sub.sort(key=lambda x: getPos(x))
            return (depth + 1) * indent + self.name + enter + "".join([x.toString(depth + 1) for x in self.sub])
        else:
            return depth * indent + self.name + enter

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
        elif self.get(self.root.NodeID) in cSubNodes:
            self.root = node
            
        for nodes in self.tree.values():    #尝试添加父节点
            aNodeID, aSubNodes = nodes.info()
            if self.get(cNodeID) in aSubNodes:  #是子节点
                node.pNodeID = aNodeID
    def get(self, nodeID):
        if nodeID == -1:
            return False
        else:
            return self.tree[nodeID]
    def getDepth(self, node:Node):
        cSubNodes = node.sub
        if cSubNodes:
            if node.depth == 0:
                self.depth = 1 + max([self.getDepth(subNode) for subNode in cSubNodes])
            return node.depth
        return 0  
    def getTreeDep(self):   # This can also init the tree
        return self.getDepth(self.root)
    
    def toString(self):
        return self.root.toString()

def printTree(i):
    myTree = Tree()
    stack = [Node("ROOT", []), '[']
    file:str = input()
    if file == '#':
        raise EOFError
    while True:
        if file == ']' or file == '*':
            ifile = stack[-1]
            l = []
            while ifile != '[':
                l.append(ifile)
                stack.pop()
                ifile = stack[-1]
            stack.pop()
            node = stack[-1]
            for x in reversed(l):
                try:
                    node.sub.append(x)
                except AttributeError:
                    pass    # WTF how does this even work
            myTree.add(node)
            if file == '*':
                break
        elif file.startswith('d'):
            stack.append(Node(file, []))
            stack.append('[')
        elif file.startswith('f'):
            stack.append(Node(file, []))
        file:str = input()
    print("DATA SET {}:".format(i) + enter + myTree.toString())

i = 1
while True:
    try:
        printTree(i)
    except EOFError:
        break
    i += 1