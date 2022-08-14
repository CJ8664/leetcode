class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # if Counter(s) != Counter(goal):
        #     return False
        return goal in (s+s)
        