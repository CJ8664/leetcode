```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [((x**2 + y**2)**0.5, i) for i,(x,y) in enumerate(points)]
        heapq.heapify(dist)
        result = []
        for _ in range(k):
            _, idx = heapq.heappop(dist)
            result.append(points[idx])
        return result
        
```
