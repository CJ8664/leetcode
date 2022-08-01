```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_sum = 0
        for num in nums:
            # negative prefix sum is not going to increase my total sum
            # so reset the left starting this num
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_so_far = max(max_so_far, curr_sum)
        return max_so_far
            
            
        
```
