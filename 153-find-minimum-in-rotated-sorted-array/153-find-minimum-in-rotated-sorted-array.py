class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            mid = (l + r) // 2
            result = min(result, nums[mid])
            
            # Mid is in the left part of two parts but r is outside 
            if nums[l] <= nums[mid] and nums[r] <= nums[mid]:
                l = mid + 1
            # Mid is in the right part of two parts but l is outside
            elif nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                r = mid - 1
            elif nums[l] <= nums[mid] <= nums[r]:
                r = mid - 1
                
        return result
        