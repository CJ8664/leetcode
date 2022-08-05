```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # This will only happen if the array is sorted to begin
            # with OR we are in the right part
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            # This mid could be the pivot / minimum element
            res = min(res, nums[m])
            # All the elements to the left are now useless
            if nums[m] >= nums[l]:
                l = m + 1
            # All the elements to the right are now useless
            else:
                r = m - 1
        return res
        
```
