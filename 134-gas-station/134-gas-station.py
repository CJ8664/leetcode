class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total, result = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total < 0:
                total = 0
                result = i + 1
        return result
                
        
        