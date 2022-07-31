class Solution:
    def rob(self, nums: List[int]) -> int:
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
            
            
        