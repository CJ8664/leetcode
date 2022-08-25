class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            # Text 1 should always be small
            return self.longestCommonSubsequence(text2, text1)
        
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(2)]
        prev_row, curr_row = 0, 1
        for i in range(len(text2)):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i]:
                    dp[curr_row][j] = 1 + dp[prev_row][j - 1]
                else: 
                    dp[curr_row][j] = max(dp[curr_row][j - 1], dp[prev_row][j])
            # Make the current state available in next iteration
            prev_row, curr_row = curr_row, prev_row
        return dp[prev_row][-1]
                    
                
                
            
        
        