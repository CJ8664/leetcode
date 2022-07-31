class Solution:
    def numDecodings(self, s: str) -> int:
        memory = {len(s): 1}
        def helper(idx):
            if idx in memory:
                return memory[idx]
            if s[idx] == "0":
                return 0
            res = helper(idx + 1)
            if idx + 1 < len(s) and (s[idx] == "1" or (s[idx] == "2" and s[idx + 1] in "0123456")):
                res += helper(idx + 2)
            memory[idx] = res
            return res
        return helper(0)
                

        