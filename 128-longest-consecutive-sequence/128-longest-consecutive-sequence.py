class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        l = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                l = max(length, l)
        return l