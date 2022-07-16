class MinHeap:
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)
        
    def push(self, val):
        heapq.heappush(self.data, val)
        
    def pop(self):
        return heapq.heappop(self.data)
    
    def getMin(self):
        if not self.data:
            return float('-inf')
        return self.data[0]
    
    def __len__(self):
        return len(self.data)
        
class MaxHeap:
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)
        
    def push(self, val):
        heapq.heappush(self.data, -1 * val)
        
    def pop(self):
        return -1 * heapq.heappop(self.data)
    
    def getMax(self):
        if not self.data:
            return float('inf')
        return -1 * self.data[0]
    
    def __len__(self):
        return len(self.data)
    
class MedianFinder:

    def __init__(self):
        self.big_heap = MinHeap()
        self.small_heap = MaxHeap()
        
    def balance_heaps(self):
        if len(self.small_heap) > len(self.big_heap):
            self.big_heap.push(self.small_heap.pop())
        if len(self.small_heap) < len(self.big_heap):
            self.small_heap.push(self.big_heap.pop())

    def addNum(self, num: int) -> None:
        if num <= self.small_heap.getMax():
            self.small_heap.push(num)
        else:
            self.big_heap.push(num)
            
        self.balance_heaps()   

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.big_heap):
            return self.small_heap.getMax()
        elif len(self.small_heap) < len(self.big_heap):
            return self.big_heap.getMin()
        else:
            return (self.small_heap.getMax() + self.big_heap.getMin()) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()