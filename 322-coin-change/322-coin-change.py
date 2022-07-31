class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for c in coins:
                rem_sum = i - c
                if rem_sum >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
                    
            
        