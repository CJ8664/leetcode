class Solution:
    def myPow(self, x: float, n: int) -> float:
        inv = False
        if n < 0:
            inv = True
        
        def helper(m):
            if m == 0:
                return 1
            if m == 1:
                return x
            temp = helper(m//2)
            temp *= temp
            if m % 2 == 1:
                temp *= x
            return temp
        t = helper(abs(n))
        return t if not inv else 1/t
        