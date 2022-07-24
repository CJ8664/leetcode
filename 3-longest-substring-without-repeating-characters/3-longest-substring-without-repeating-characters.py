class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        l, r = 0, 0
        max_substring = 0
        while r < len(s):
            if s[r] not in seen_set:
                seen_set.add(s[r])
                r += 1
                max_substring = max(max_substring, len(seen_set))
            else:
                while l < r and s[r] in seen_set:
                    seen_set.remove(s[l])
                    l += 1
        return max_substring
        