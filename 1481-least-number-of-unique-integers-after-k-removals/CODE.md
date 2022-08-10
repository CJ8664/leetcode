```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        h = list(c.values())
        heapq.heapify(h)
        for _ in range(k):
            v = heapq.heappop(h)
            if v - 1 > 0: heapq.heappush(h, v - 1)
        return len(h)
            
        
```
