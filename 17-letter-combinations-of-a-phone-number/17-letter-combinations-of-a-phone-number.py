class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        
        dialpad_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
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
                
            
                
        