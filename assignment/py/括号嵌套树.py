class Node(object):
    NodeID:str
    pNodeID:str
    sub:list
    def __init__(self, NodeID, l, pNodeID= ''):
        self.NodeID = NodeID
        self.pNodeID = pNodeID
        self.sub = []
        for node in l:
            self.sub.append(node)
    def __str__(self):  #Debug
        return "🌿{} p:{}, s:{}".format(self.NodeID, self.pNodeID, self.sub)
    def info(self):
        return (self.NodeID, self.sub)
    
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
        elif self.root.NodeID in cSubNodes:
            self.root = node
            
        for nodes in self.tree.values():    #尝试添加父节点
            aNodeID, aSubNodes = nodes.info()
            if cNodeID in aSubNodes:  #是子节点
                node.pNodeID = aNodeID
    def get(self, nodeID):
        if nodeID == "":
            return False
        else:
            return self.tree[nodeID]
    def getDepth(self, node:Node):
        cSubNodes = node.sub
        if cSubNodes:
            return(1 + max([self.getDepth(self.get(subNode)) for subNode in cSubNodes]))
        return 1  
    def getTreeDep(self):
        return self.getDepth(self.root)
    
    def preorderFrom(self, node:Node):  # 先序遍历
        return node.NodeID + "".join([self.preorderFrom(self.get(x)) for x in node.sub])
    def preorder(self):
        return self.preorderFrom(self.root)
    def postorderFrom(self, node:Node):  # 后序遍历
        return "".join([self.postorderFrom(self.get(x)) for x in node.sub]) + node.NodeID
    def postorder(self):
        return self.postorderFrom(self.root)
    
    
    
def getTreeFromString(stree:str):
    outTree = Tree()
    if len(stree) == 1:
        node = Node(stree, [])
        outTree.add(node)
        outTree.root = node
        return outTree
    stack = []
    for char in stree:
        if char == ')':
            ichar = stack[-1]
            l = []
            while ichar != '(':
                l.append(ichar)
                stack.pop()
                ichar = stack[-1]
            stack.pop()
            for x in l:
                if not x in outTree.tree.keys():
                    outTree.tree[x] = Node(x, [])
            node = Node(stack[-1], reversed(l))
            outTree.add(node)
        elif char == ',':
            continue
        else:
            stack.append(char)
    return outTree


myTree = getTreeFromString(input())
print(myTree.preorder() + "\n" + myTree.postorder())