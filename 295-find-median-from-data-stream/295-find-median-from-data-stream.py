class MaxHeap:
    """pop returns min"""
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)
        
    def push(self, val):
        heapq.heappush(self.data, -1 * val)
        
    def pop(self):
        return -1 * heapq.heappop(self.data)
    
    def get_max(self):
        return -1 * self.data[0] if self.data else float('-inf')

    def __len__(self):
        return len(self.data)
    
class MinHeap:
    """pop returns min"""
    def __init__(self):
        self.data = []
        heapq.heapify(self.data)
        
    def push(self, val):
        heapq.heappush(self.data, val)
        
    def pop(self):
        return heapq.heappop(self.data)
    
    def get_min(self):
        return self.data[0] if self.data else float('inf')
    
    def __len__(self):
        return len(self.data)

class MedianFinder:

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()
        
    def balance_heaps(self):
        if len(self.left) > len(self.right):
            self.right.push(self.left.pop())
        elif len(self.left) < len(self.right):
            self.left.push(self.right.pop())

    def addNum(self, num: int) -> None:
        if num > self.left.get_max():
            self.right.push(num)
        else:
            self.left.push(num)
        
        self.balance_heaps()

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left.get_max()
        elif len(self.left) < len(self.right):
            return self.right.get_min()
        else:
            return (self.left.get_max() + self.right.get_min()) / 2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()