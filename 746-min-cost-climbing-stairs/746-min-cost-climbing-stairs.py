class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            # To cost[i] represents the cost you need to pay to get to next
            # step starting from i.
            # But to get to step i, you need to pay some cost. 
            # That is pay the cost from 
            # - second last step and take two steps
            # - last step and take one step
            cost[i] += min(cost[i-2], cost[i-1])
        return min(cost[-1], cost[-2])
            
            
        