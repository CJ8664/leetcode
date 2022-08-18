class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total = len(small) + len(big)
        half = total // 2
        
        l, r = 0, len(small) - 1
        
        while True:
            i = (l + r) // 2 # leftmost index in the left part of small array
            j = half - i - 2 # Number of elements in left part of big array
            
            small_left = small[i] if i >= 0 else float('-inf') 
            small_right = small[i + 1] if (i + 1) < len(small) else float('inf')
            big_left = big[j] if j >= 0 else float('-inf') 
            big_right = big[j + 1] if (j + 1) < len(big) else float('inf')
            
            # The small array is partitioned correctly
            if small_left <= big_right and big_left <= small_right:
                # even total len
                if total % 2 == 0:
                    return (max(small_left, big_left) + min(small_right, big_right)) / 2
                # odd case
                return min(small_right, big_right)
            # Took extra elements from small
            elif small_left > big_right: 
                r = i - 1
            # Took less elements from small
            else:
                l = i + 1
                
                    