class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                # -1 to consider the infinity that we added at begin
                # of array
                return mid - 1
            elif nums[mid - 1] < nums[mid] < nums[mid + 1 ]:
                l = mid + 1
            else:
                r = mid - 1
        # Either points to index 0 or len(nums) - 1 in original array
        return l
        