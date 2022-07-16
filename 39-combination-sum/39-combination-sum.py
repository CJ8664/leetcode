class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def dfs(idx, rem_sum):
            if rem_sum < 0 or idx >= len(candidates):
                return
            elif rem_sum == 0:
                result.append(subset.copy())
                return
  
            # pick the element, we are not doing idx + 1 
            # coz we can repeat the number
            subset.append(candidates[idx])
            dfs(idx, rem_sum - candidates[idx])                

            # Dont pick the element
            subset.pop()
            dfs(idx + 1, rem_sum)
                

        dfs(0, target)       
        return result
            
        