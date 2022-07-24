class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        result = 0
        for n in nums:
            if n not in n_set:
                continue
            n_set.remove(n)
            # count left
            n_l, c_l = n, 0
            while n_l - 1 in n_set:
                c_l += 1
                n_set.remove(n_l - 1)
                n_l -= 1
            # count right
            n_r, c_r = n, 0
            while n_r + 1 in n_set:
                c_r += 1
                n_set.remove(n_r + 1)
                n_r += 1
            result = max(result, c_l + 1 + c_r)
        return result
        