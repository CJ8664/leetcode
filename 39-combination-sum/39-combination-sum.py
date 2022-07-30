class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()
        
        def dfs(idx, curr_sum):
            if curr_sum > target or idx >= len(candidates):
                return
            if curr_sum == target:
                result.append(copy.copy(subset))
                return
            
            subset.append(candidates[idx])
            dfs(idx, curr_sum + candidates[idx])
            
            subset.pop()
            dfs(idx + 1, curr_sum)

        dfs(0, 0)
        return result
                
            
                
            
        