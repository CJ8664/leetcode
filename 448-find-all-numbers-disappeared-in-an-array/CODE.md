```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark indexes pointed by numbers as negative
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        result = []
        # The indexes that have not been marked are missing
        for idx in range(len(nums)):
            if nums[idx] > 0:
                result.append(idx + 1)
        return result
                
        
```
