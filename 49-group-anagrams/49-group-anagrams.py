class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            key = [0 for _ in range(26)]
            for c in s: 
                key[ord(c) - ord('a')] += 1
            key = "".join([chr(ord("a") + i) + str(x) for i, x in enumerate(key) if x > 0])
            if key not in result:
                result[key] = []
            result[key].append(s)
        return list(result.values())
        