class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                l = 1
                while (n + l) in numSet:
                    l += 1
                longest = max(l, longest)
        return longest