class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        
        dialpad_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        result, combs = [], []
        def backtracking(idx):
            if idx >= len(digits):
                result.append("".join(combs))
                return
            for ch in dialpad_map[digits[idx]]:
                combs.append(ch)
                backtracking(idx + 1)
                combs.pop()
        backtracking(0)
        return result
                
            
                
        