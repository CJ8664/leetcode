class Solution:
    def jump(self, nums: List[int]) -> int:  
        # from the current element in the window find the
        # farthest index that you can jump. That becomes
        # the end point of the next window
        # Number of windows is the result
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
        