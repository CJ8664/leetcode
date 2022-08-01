class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            lsb = n & 1
            n = n >> 1
            result = result | lsb
            result = result << 1
        return result >> 1
        