```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # necessary so that we can compare the end of left with
        # start of right interval
        intervals.sort()
        result = []
        for idx in range(len(intervals) - 1):
            left, right = intervals[idx], intervals[idx + 1]
            # Left interval ends before the start of right interval
            if left[1] < right[0]:
                result.append(left)
            else:
                intervals[idx + 1][0] = min(left[0], right[0])
                intervals[idx + 1][1] = max(left[1], right[1])
        result.append(intervals[-1])
        return result
                
        
```
