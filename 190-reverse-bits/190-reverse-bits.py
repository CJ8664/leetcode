class Solution:
    def reverseBits(self, n: int) -> int:
        # Get the LSB and keep appending to result.
        # while result shifts to the left the lsb is 
        # always appended as result's so over time by left 
        # shift it becomes msb
        result = 0
        for _ in range(32):
            lsb = n & 1
            n = n >> 1
            result = result | lsb
            result = result << 1
        return result >> 1
        