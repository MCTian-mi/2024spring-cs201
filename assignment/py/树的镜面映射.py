class Node:
    _ID=0
    id:int
    name:str
    sub:list
    
    def __init__(self, name, sub):
        self.id = self.__class__._ID
        self.__class__._ID += 1
        self.name = name
        self.sub = sub
    def isFake(self):
        return self.name == '$'
    
def levelOrder(root:Node):
    l = [[]]
    def pseudoLeverParser(node:Node, l:list, level:int):
        if node is None or node.isFake(): return
        try:
            l[level].append(node)
        except IndexError:
            l.append([node])
        pseudoLeverParser(node.sub[0], l, level + 1)
        pseudoLeverParser(node.sub[1], l, level)
    pseudoLeverParser(root, l, 0)
    return ' '.join(''.join([''.join([y.name for y in reversed(x)]) for x in l]))
        
n = int(input())
l = input().split()
stack = []
root = None
for x in l[::-1]:
    name, nodetype = x[0], int(x[1])
    if nodetype:
        stack.append(Node(name, [None, None]))
    else:
        node1 = stack.pop()
        node2 = stack.pop()
        neonode = Node(name, [node1, node2])
        stack.append(neonode)
        root = neonode
ans = levelOrder(root)
print(ans)