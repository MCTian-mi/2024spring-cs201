class queue(list):
    def _enqueue(self, i):
        self.append(i)
    def _dequeue(self):
        x = self[0]
        self.pop(0)
        return x

class queues(list):
    listl = list
    array:dict
    def __init__(self):
        self.array = dict()
        self.listl = list()
    def add(self, l):
        self.append(queue())
        for x in l:
            self.array[x] = i
    def op(self, arg, x = 0):
        x = int(x)
        if arg == 'ENQUEUE':
            y = self.array[x]
            if y not in self.listl:
                self.listl.append(y)
            self[y]._enqueue(x)
        elif arg == 'DEQUEUE':
            for q in self.listl:
                if self[q] == []:
                    pass
                else:
                    print(self[q]._dequeue())
                    break
        else:
            raise EOFError

myQueues = queues()
for i in range(int(input())):
    myQueues.add(list(map(int, input().split())))
while 1:
    try:
        myQueues.op(*input().split())
    except EOFError:
        break