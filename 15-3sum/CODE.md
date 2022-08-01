```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the nums to handle duplicates
        nums.sort()
        result = []
        for i in range(len(nums)):
            # if anchor element is same skip. Eg [1,1, 2, 3] 1 is duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            # Find the other elements in remainder of the array
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Same de-duplication logic in the "remainder array"
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return result
                    
            
        
```
