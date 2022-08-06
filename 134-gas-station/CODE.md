```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost then we can never
        # complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        total, result = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total < 0:
                total = 0
                # If we cannot start the journey from i
                # then we might be able to start from i+1
                result = i + 1
        return result
                
        
        
```
