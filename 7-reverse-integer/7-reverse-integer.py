class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x) if is_neg else x
        res = 0
        while x > 0:
            res *= 10
            res += x % 10
            x = x // 10
        MAX = 0x80000000 
        MIN = 0x7FFFFFFF
        if not is_neg:
            res = res if res < MAX else 0
        else:
            res = -res if res < MIN else 0
        return res
        