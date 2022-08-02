```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Trick way
        # 6 --> 110, 13 --> 1101 --> 110-1
        # so bits in 6 + lsb 
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
        
        # Loops and pattern way
        num_bits = [0 for _ in range(n + 1)]
        counter, i = 1, 1
        while i < len(num_bits):
            c = 0
            while c < counter and i < len(num_bits):
                num_bits[i] = 1 + num_bits[i - counter]
                i, c = i + 1, c + 1
            counter *= 2
        return num_bits
            
        
```
