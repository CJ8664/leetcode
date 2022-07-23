class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))] 
        l_prefix, r_prefix = 1, 1
        for i in range(1, len(nums)):
            l_prefix *= nums[i - 1]
            result[i] *= l_prefix
        for i in range(len(nums) - 2, -1, -1):
            r_prefix *= nums[i + 1]
            result[i] *= r_prefix
        return result
            
        
        
        