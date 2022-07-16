class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        
        def backtrack(idx):
            # we have reached end of traveral
            if idx >= len(nums):
                result.append(copy.copy(subset))
                return
                           
            # pick the element
            subset.append(nums[idx])
            backtrack(idx + 1)

            # IF we decide dont pick the element, we should also not pick any
            # of it duplicates
            subset.pop()
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1) #  + 1 to hit the recursion base condition
            
        backtrack(0)
        return result