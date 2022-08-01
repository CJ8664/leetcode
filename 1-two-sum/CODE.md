```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for idx, num in enumerate(nums):
            cand = target - num
            if cand in pos:
                return [pos[cand], idx]
            pos[num] = idx
        
        
```
