class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j, n = 0, 0, 0
        while j < len(arr):
            n += 1
            if n != arr[j]:
                k -= 1
            else:
                j += 1
            if k == 0:
                return n
        for _ in range(k):
            n += 1
        return n
        