class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            key = [0 for _ in range(26)]
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        return list(result.values())
        