```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
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
        
        result = []
        def backtracking(idx, curr_str):
            if len(curr_str) == len(digits):
                result.append(curr_str)
                return
            # Pick a character one by one for number 2, and find all the 
            # chars that can be used from 3 in the input '23' and so on
            for ch in dialpad_map[digits[idx]]:
                backtracking(idx + 1, curr_str + ch)
                
        if digits:      
            backtracking(0, "")
        return result
                
            
                
        
```
