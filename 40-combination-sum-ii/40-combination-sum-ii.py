class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Runtime complexity: for every element 'n' we have two choice, to pick or not to pick.
        # So 2 x 2 x 2.. = n x 2**n
        candidates.sort()
        result = []
        subset = []
        def backtrack(idx, rem_sum):
            print(idx, rem_sum, subset)
            if rem_sum == 0:
                result.append(copy.copy(subset))
                return 
            if rem_sum < 0 or idx >= len(candidates):
                return 

            # pick the element
            subset.append(candidates[idx])
            backtrack(idx + 1, rem_sum - candidates[idx])
            
            # if we dont pick the element skip all the duplicate elements
            subset.pop()
            while (idx + 1) < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1, rem_sum) # +1 to hit the base condition of the recursion
        backtrack(0, target)
        return result
            
        