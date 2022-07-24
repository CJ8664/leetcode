class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        l, r = 0, 0
        max_substring = 0
        while r < len(s):
            # If new character add it to the substring
            if s[r] not in seen_set:
                seen_set.add(s[r])
                r += 1
                max_substring = max(max_substring, len(seen_set))
            # remove the left part of the current substring till the 
            # new char at 'r' can be added to form a new substring
            else:
                while l < r and s[r] in seen_set:
                    seen_set.remove(s[l])
                    l += 1
        return max_substring
        