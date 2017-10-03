#!/usr/local/bin/python

# Problem URL : https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        counter = 0
        while(i < len(nums)-counter):
            if nums[i] == 0:
                # Move all elements left 
                while(j<len(nums)-counter-1):
                    nums[j] = nums[j+1]
                    j +=1
                nums[j] = 0
                counter +=1
            #print(str(nums))
            if nums[i] != 0:
                i +=1
            j = i