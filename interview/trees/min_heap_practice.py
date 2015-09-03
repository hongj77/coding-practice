class MinHeap():
    def __init__(self):
        self.heap = [0]
        self.size = 0
    def insert(self,val):
        self.heap.append(val)
        self.count += 1
        i = self.size
        self.percUp(i)
    def percUp(self,i):
        while i/2 > 0: #while the parent of the node is at least root
            if self.heap[i] < self.heap[i/2]:
                self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
            i = i/2
    def pop(self):
        minVal = self.heap[1]
        self.heap[1] = self.heap[heap.size]
        self.heap.pop()
        self.size -= 1
        percDown(1)
        return minVal
    def percDown(self,i):
        while i*2 <= self.size:
            mc = minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
    def minChild(self,i):
        if 2*i + 1 > self.size:
            return 2*i
        elif self.heap[2*i + 1] < self.heap[2*i]:
            return 2*i+1
        else:
            return 2*i
    def buildHeap(ls):
        self.size = len(ls)
        self.heap = [0] + ls[:]
        i = self.size / 2
        while i > 0:
            self.percDown(i)
            i -= 1



