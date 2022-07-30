class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr_elements = []
        candidates.sort()
        def dfs(curr_sum, idx):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(copy.copy(curr_elements))
                return
            for i in range(idx, len(candidates)):
                can = candidates[i]
                curr_elements.append(can)
                dfs(curr_sum + can, i)
                curr_elements.pop()
                if curr_sum + can > target:
                    break
        dfs(0, 0)
        return result
                
            
                
            
        