```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        i = 0 
        while i < len(intervals) - 1:
            # curr interval less than next
            if intervals[i][1] < intervals[i + 1][0]:
                result.append(intervals[i])
            else:
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
            i += 1
        result.append(intervals[-1])
        return result
                
            
            
            
        
        
```
