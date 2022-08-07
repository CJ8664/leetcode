class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        result = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                result.append(idx + 1)
        return result
                
        