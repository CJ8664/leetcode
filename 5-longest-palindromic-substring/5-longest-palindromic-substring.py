class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for start in range(len(s)):
            l, r = start, start
            print(start)
            even = False
            while 0 <= l and r < len(s):
                if l == start and r < len(s) - 1 and s[l] == s[r + 1]:
                    r += 1
                    continue
                elif s[l] == s[r]:
                    l -= 1
                    r += 1
                    continue
                break            
            result = s[l+1:r] if len(s[l+1:r]) > len(result) else result
            print(r, l, result)
        return result

        