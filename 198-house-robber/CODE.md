```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        ########################
        ###### DP approach #####
        ########################
        
        # Rob 1 represents that you didn't rob last hous
        # Rob 2 represents that you robbed last house
        rob1, rob2 = 0, 0

        for n in nums:
            # For a given house, temp represents the max 
            # you can rob which is 
            # if you rob this and not the previous: n + rob1
            # if you dont rob this since you robbed last: rob2
            temp = max(n + rob1, rob2)
            # If we didnt rob this house rob2 respresents rob1
            rob1 = rob2
            # If we did rob this house rob2 represent temp
            rob2 = temp
        # rob2 represents the maximum for last house
        return rob2
        
        ########################
        ## Backtrack approach ##
        ########################
        memory = {}
        def backtrack(pos):
            if pos >= len(nums):
                return 0
            
            # If we have visited the house before we know the maximum
            # money we can rob from this point onwards
            if pos in memory:
                return memory[pos]
            
            # at a given position we have two possibilities
            # rob house or dont. if robbed house then the
            # next house should be skipped ELSE next house should be 
            # robbed
    
            # Not robbed
            res1 = backtrack(pos + 1)
            # Robbed
            res2 = backtrack(pos + 2)
            res = max(res1, res2 + nums[pos])
            memory[pos] = res
            return res
        return backtrack(0)
            
            
        
```
