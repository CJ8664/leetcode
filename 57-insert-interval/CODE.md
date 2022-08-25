```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, interval in enumerate(intervals):
            # new interval ends before start of interval
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            # interval ends before new interval
            elif interval[1] < newInterval[0]:
                result.append(interval)
            # new interval is overlapping
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            
        result.append(newInterval)
        return result
                
                    
            
            
            
            
```
