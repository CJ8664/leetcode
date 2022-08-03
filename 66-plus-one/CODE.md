```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            carry, digits[idx] = divmod(carry + digits[idx], 10)
        return digits if carry == 0 else [1] + digits
            
        
```
