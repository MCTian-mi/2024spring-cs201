enter = '\n'

def parse(dic: dict, root: int) -> str:
    y = dic[root] + [root]
    y.sort()
    for x in y:
        if x != root:
            parse(dic, x)
        else:
            print(x)

myTree = dict()
root = None
for _ in range(int(input())):
    nodel = list(map(int, input().split()))
    nodename = nodel[0]
    if root is None:
        root = nodename
    xl = nodel[1:]
    myTree[nodename] = xl
    flag = True
    while flag:
        for key in myTree.keys():
            if root in myTree[key]:
                root = key
                flag = not flag
                break
        flag = not flag
        
parse(myTree, root)