class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            # Text 1 should always be small
            return self.longestCommonSubsequence(text2, text1)
        
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(2)]
        for i in range(len(text2)):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i]:
                    dp[1][j] = 1 + dp[0][j - 1]
                else: 
                    dp[1][j] = max(dp[1][j - 1], dp[0][j])
            # Make the current state available in next iteration
            for x in range(len(text1) + 1):
                dp[0][x] = dp[1][x]
        return dp[1][-1]
                    
                
                
            
        
        