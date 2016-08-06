class Heap():

    def __init__(self):
        self.heapList = []
        self.size = 0

    def buildHeap(self, arr):
        for i, each in enumerate(arr):
            self.heapList.append(each)
            self.size += 1
            self.bubbleUp(self.size)

    def bubbleUp(self, size):
        i = size - 1
        while i > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i -= 1

    def bubbleDown(self):
        i = 0
        while i <= (self.size - 1) // 2:
            sc = self.smallestChild(i)
            if i == 0 and self.size > 1:
                self.heapList[0], self.heapList[1] = self.heapList[1], self.heapList[0]
            elif self.heapList[i] > self.heapList[sc]:
                self.heapList[i], self.heapList[
                    sc] = self.heapList[sc], self.heapList[i]
            else:
                break
            i = sc

    def insert(self, val):
        self.heapList.append(val)
        self.size += 1
        self.bubbleUp(self.size)

    def extractMin(self):
        n = self.size - 1
        self.heapList[0], self.heapList[n] = self.heapList[n], self.heapList[0]
        retval = self.heapList.pop()
        self.size -= 1
        self.bubbleDown()
        return retval

    def smallestChild(self, i):
        if self.size == 1:
            return 0
        elif self.size == 2:
            return 1 if self.heapList[0] > self.heapList[1] else 0
        elif self.size == 3:
            return 1 if self.heapList[1] < self.heapList[2] else 2

        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def peek_root(self):
        return self.heapList[0]