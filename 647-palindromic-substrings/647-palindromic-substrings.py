class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        def is_palindrome(l, r):
            nonlocal result
            while 0 <= l and r < len(s):
                if s[l] != s[r]:
                    break
                l, r = l - 1, r + 1
                result += 1
    
        for idx in range(len(s)):
            # odd length
            is_palindrome(idx, idx)
            # even length
            is_palindrome(idx, idx + 1)
        return result
            
        