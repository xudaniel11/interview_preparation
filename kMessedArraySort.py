"""
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time.
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Algorithm: start by initializing minheap. Move through array in chunks of size K. During each iteration/chunk, remove min value from window/heap
and then write min value at the left of the chunk. Then, insert into the heap the next value in the array. Once we can't move through
the array anymore, pop off the minvalues in the heap and overwrite in original array. 

Time Analysis: O(k*logk) to initally build heap. 
O(1) to append a new, unsorted value into heap, and O(log k) to bubble it up. 
O(1) to pop min value from heap, and O(log k) to bubble down new root.
Do the above inserting and/or popping ~N times.
O(1) to overwrite value in array.
So, final time complexity is O(N*logk). 
"""


def kMessedArraySort(arr, k):
    if k == 0:
        return arr
    n = len(arr)
    heap = Heap()
    heap.buildHeap(arr[:k+1])
    arr[0] = heap.extractMin()
    for i in range(1, n - k):
        heap.insert(arr[i + k])
        indexOfElemToSwap = arr.index(heap.extractMin())
        arr[i], arr[indexOfElemToSwap] = arr[indexOfElemToSwap], arr[i]

    lastInsert = n - k
    while heap.size > 0:
        arr[lastInsert] = heap.extractMin()
        lastInsert += 1
    return arr


# MinHeap: every node is smaller than its children
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
                self.heapList[i], self.heapList[
                    i // 2] = self.heapList[i // 2], self.heapList[i]
            i -= 1

    def bubbleDown(self):
        i = 0
        while i <= (self.size - 1) // 2:
            sc = self.smallestChild(i)
            if i == 0 and self.size > 1:
                if self.heapList[0] > self.heapList[1]:
                    self.heapList[0], self.heapList[
                        1] = self.heapList[1], self.heapList[0]
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


def testHeap():
    heap = Heap()
    arr = [7, 6, 5, 4, 3, 2, 1]
    heap.buildHeap(arr)
    print heap.heapList
    heap.extractMin()
    print heap.heapList


def testKMessed():
    arr0 = [1, 5, 9, 6, 3, 7]
    print kMessedArraySort(arr0, 3)
    arr1 = [5, 2, 1, 6, 7, 4, 3]
    print kMessedArraySort(arr1, 4)
    arr2 = [1]
    print kMessedArraySort(arr2, 0)
    arr3 = [-4, 5, 1]
    print kMessedArraySort(arr3, 1)

testKMessed()
