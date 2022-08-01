```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        m, result, current_product = abs(n), 1, x
        while m > 0:
            if m % 2 == 1:
                result *= current_product
            current_product *= current_product
            m = m // 2
        return result if n > 0 else 1 / result
        
```
