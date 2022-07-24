class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prefix = prices[0]
        max_profit = 0 
        for price in prices:
            max_profit = max(price - min_prefix, max_profit)
            min_prefix = min(min_prefix, price)
        return max_profit
            
        
        