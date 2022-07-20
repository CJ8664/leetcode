class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        result = 1
        current_product = x
        while m > 0:
            if m % 2 == 1:
                result *= current_product
            current_product *= current_product
            m = m // 2
        return result if n > 0 else 1 / result
        