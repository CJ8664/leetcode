class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # There can be infinite ways to arrange a given amount 
        # as a default value
        dp = [float('inf') for _ in range(amount + 1)]
        # Minimum way to get to total 0 is 0 ( pick no coin )
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                # If i select this coin, what is the minimum number
                # of ways to pick coins for remaining sum. If in the 
                # coins list I find a minimum that is less than
                # number of way for a previous coin then min with self
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        # If no soulution found for amount instead of passing our
        # default, pass -1 as specified in the question
        return dp[amount] if dp[amount] != float('inf') else -1
                    
            
        