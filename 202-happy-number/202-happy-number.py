class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            new_n = 0
            while n > 0:
                n, d = divmod(n, 10)
                new_n += d ** 2
            n = new_n
        return True
        