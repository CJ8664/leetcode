class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        one_step, two_step = 1, 2
        for _ in range(3, n + 1):
            one_step, two_step = two_step, (one_step + two_step)
        return two_step
            
        