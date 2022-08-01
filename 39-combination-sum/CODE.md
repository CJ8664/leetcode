```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        
        # Required for pruning logic of the DFS + Bactracking
        candidates.sort()
        
        def dfs(curr_sum, curr_idx):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(copy.copy(subset))
                return
            
            for idx in range(curr_idx, len(candidates)):
                # Add the current element 
                subset.append(candidates[idx])
                # and try to see if we find a solution
                dfs(curr_sum + candidates[idx], idx)
                # Backtrack and see if there are other solution
                subset.pop()
                
                # Pruning logic, if the current candidate is not 
                # part of solution, all the elements after that
                # are going to be bigger and hence not going to be
                # part of solution as well
                if curr_sum + candidates[idx] > target:
                    break
                    
        dfs(0, 0)
        return result
                
                
                
            
                
            
        
```
