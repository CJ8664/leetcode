class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while n not in seen_numbers:
            seen_numbers.add(n)
            s = 0
            while n > 0:
                s += (n % 10)**2
                n = n // 10
            if s == 1:
                return True
            n = s
        return False
        