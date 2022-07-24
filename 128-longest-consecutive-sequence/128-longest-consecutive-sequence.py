class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for n in nums:
            if (n - 1) not in num_set:
                curr_num, curr_len = n, 1
                while curr_num + 1 in num_set:
                    curr_len += 1
                    curr_num += 1
                result = max(curr_len, result)
        return result