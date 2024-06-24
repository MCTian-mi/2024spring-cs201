class BinHeap(list):
    def insert(self, __object) -> None:
        super().append(__object)
        index = len(self) - 1
        self._siftup(index)
    def pop(self):
        x = self[-1]
        del(self[-1])
        if self:
            self[0] = x
            self._sinkdown(0)
    
    def _swap(self, index1, index2) -> None:
            self[index1], self[index2] = self[index2], self[index1]
    def _siftup(self, index) -> None:
        pIndex = (index - 1)//2
        if pIndex >= 0 and self[pIndex] > self[index]:
            self._swap(pIndex, index)
            return self._siftup(pIndex)
        return
    def _sinkdown(self, index) -> None:
        lIndex = 2 * index + 1
        rIndex = lIndex + 1
        s = self[index]
        try:
            l = self[lIndex]
            mIndex = lIndex
            try:
                r = self[rIndex]
                if r < l:
                    mIndex = rIndex
            except IndexError:
                pass
            if self[mIndex] < s:
                self._swap(mIndex, index)
                return self._sinkdown(mIndex)
        except IndexError:
            pass
        return
        
    def popAndReturn(self) -> int:
        x = self[0]
        self.pop()
        return x
    def op(self, op, element=None):
        if op == 1:
            self.insert(element)
        else:
            print(self.popAndReturn())
    
n = int(input())
myBinHeap = BinHeap()
for _ in range(n):
    myBinHeap.op(*map(int, input().split()))