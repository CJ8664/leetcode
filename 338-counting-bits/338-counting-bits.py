class Solution:
    def countBits(self, n: int) -> List[int]:
        num_bits = [0 for _ in range(n + 1)]
        counter, i = 1, 1
        while i < len(num_bits):
            c = 0
            while c < counter and i < len(num_bits):
                num_bits[i] = 1 + num_bits[i - counter]
                i, c = i + 1, c + 1
            counter *= 2
        return num_bits
            
        