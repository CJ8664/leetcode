class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            idx = abs(num) - 1
            # If we are trying to mark a number that is already 
            # negative it means that we have seen that index 
            # before and hence the number is duplicate
            if nums[idx] < 0:
                result.append(idx + 1)
            # Seeing index for first time, mark negative
            else:
                nums[idx] *= -1
        return result
            
        