class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        def max_palindrome(l, r):
            nonlocal result
            while 0 <= l and r < len(s):
                if s[l] != s[r]:
                    break
                l, r = l - 1, r + 1
            if r - l - 1 > len(result):
                result = s[l + 1:r]

        for idx in range(len(s)):
            # odd length
            max_palindrome(idx, idx)
            # even length
            max_palindrome(idx, idx + 1)
        return result

        