class Solution:        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(l, r):
            p = nums[(l + r)//2]
            while l <= r:
                while nums[l] < p: l += 1
                while nums[r] > p: r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l, r = l + 1, r - 1
            return l
        
        def quickselect(start, end):
            if start < end:
                part = partition(start, end)
                if part <= len(nums)-k:
                    quickselect(part, end)
                else:
                    quickselect(start, part-1)
        

        quickselect(0, len(nums)-1)
        return nums[len(nums)-k]
        