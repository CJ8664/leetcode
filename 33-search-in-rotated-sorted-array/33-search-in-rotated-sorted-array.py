class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left sorted portion
            if nums[l] <= nums[mid]:
                # number is on the right side OR number is on the right side because of partition
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # number is still in the left sorted part
                else:
                    r = mid - 1
            # Right sorted part
            else:
                # number is on the left side OR number is on left side because of partition
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # number is still in the right part
                else:
                    l = mid + 1
        return -1