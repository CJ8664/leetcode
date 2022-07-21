class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum += num
            if curr_sum < num:
                curr_sum = num
            max_so_far = max(max_so_far, curr_sum, num)
        return max_so_far
            
            
        