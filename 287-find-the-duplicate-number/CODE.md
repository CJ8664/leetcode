```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Marking 
        for num in nums:
            i = abs(num)
            if nums[i] > 0:
                nums[i] *= -1
            # The num represents an index, and the value pointed by it
            # is already makred negative. Means we are seeing num
            # again and hence is the duplicate
            else:
                return i
                
        # Floyd's Tortoise and Hare (Cycle Detection)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
```
