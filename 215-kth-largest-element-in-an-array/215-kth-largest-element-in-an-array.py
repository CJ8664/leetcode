class Solution:
    def partition(self, arr, start, end):
        pivot = arr[(start + end)//2]
        i = start
        j = end
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
        return i

    def quicksort(self, arr, start, end, k):
        if start < end:
            
            part = self.partition(arr, start, end)
            if part <= len(arr)-k:
                self.quicksort(arr, part, end, k)
            else:
                self.quicksort(arr, start, part-1, k)
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums == None:
            return None
        if len(nums) == 1:
            return nums[0]
        else:
            self.quicksort(nums, 0, len(nums)-1, k)
            return nums[len(nums)-k]
        
        
        