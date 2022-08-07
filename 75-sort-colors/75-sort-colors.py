class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### THIS IS ONE PASS SOLUTION ######
        ### Other solution is bucket sort ##
        ####################################
        l, r, i = 0, len(nums) - 1, 0        
        while i <= r:
            # IF current num is 0 then swap it with the position 
            # pointed by l
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            # If current num is 2 then swap it with the position 
            # pointed by r
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # We could swap a 0 from right side and then if 
                # increment i, it will never be processed hence 
                # decrement i to offset with the increment outside
                # if-else
                i -= 1
            i += 1
                
        
        
        