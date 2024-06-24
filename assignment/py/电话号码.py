class PrefixError(IndexError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Node:
    _ID=0
    id:int
    is_word:bool
    name:str
    sub:list
    
    def __init__(self, name, sub, is_word=False):
        self.id = self.__class__._ID
        self.__class__._ID += 1
        self.name = name
        self.sub = sub
        self.is_word = is_word
    def mark_word(self):
        self.is_word =True
    
class Tree:
    root:Node
    
    def __init__(self) -> None:
        self.root = Node('', [])
    def push(self, string):
        flag = self._push(string, self.root, False)
        if not flag:
            raise PrefixError
    def _push(self, string:str, node:Node, flag):
        if not string:
            node.mark_word()
            return flag
        this, remaining = string[0], string[1:]
        for subnode in node.sub:
            if this ==subnode.name:
                if subnode.is_word: raise PrefixError
                return self._push(remaining, subnode, flag)
        neonode = Node(this, [])
        node.sub.append(neonode)
        return self._push(remaining, neonode, True)

def check(times, tree):
    flag = True
    for _ in range(times):
        x = input()
        if not flag: continue
        try:
            tree.push(x)
        except PrefixError:
            flag = False
    print(['NO', 'YES'][flag])
    return

t = int(input())
for _ in range(t):
    myTree = Tree()
    check(int(input()), myTree)