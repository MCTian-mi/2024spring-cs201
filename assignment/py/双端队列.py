class deque(object):
    dequeList:list
    
    def __init__(self):
        self.dequeList = []
    def __str__(self):
        if self.dequeList:
            return (' '.join(str(T) for T in self.dequeList))
        else:
            return "NULL"
    def append(self, T):
        self.dequeList.append(T)
    def appendLeft(self, T):
        self.dequeList.insert(0, T)
    def pop(self):
        self.dequeList.pop()
    def popLeft(self):
        self.dequeList.pop(0)

def op(dequeIn:deque, operatorType:int, t:int):
    if operatorType == 1:
        dequeIn.append(t)
    elif t == 0:
        dequeIn.popLeft()
    else:
        dequeIn.pop()
  
for _ in range(int(input())):
    dequeI = deque()
    for __ in range(int(input())):
        operatorType, t = map(int, input().split())
        op(dequeI, operatorType, t)
    print(dequeI)
