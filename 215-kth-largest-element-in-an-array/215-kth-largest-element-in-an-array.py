class Solution:        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        def partition(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p
        
        l, r = 0, len(nums) - 1
        while True:
            p = partition(l, r)
            if p < k:
                l = p + 1
            elif p > k:
                r = p - 1
            else:
                return nums[p]
        