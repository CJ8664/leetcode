```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in {num1, num2}:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                temp = int(num1[i1]) * int(num2[i2]) + res[i1 + i2]
                res[i1 + i2] = temp % 10
                res[i1 + i2 + 1] += temp // 10
        while res[-1] == 0: res.pop()
        return "".join([str(x) for x in res[::-1]])
                
                
                
                
        
```
