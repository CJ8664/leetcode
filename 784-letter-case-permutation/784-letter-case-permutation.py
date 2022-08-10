class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def helper(idx):
            if idx == len(s):
                return [""]
            res = []
            for x in helper(idx + 1):
                if s[idx].isalpha():
                    res.append(s[idx] + x)
                    res.append(s[idx].swapcase() + x)
                else:
                    res.append(s[idx] + x)
            return res
        return helper(0)
                    
            
        