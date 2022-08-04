class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(x**2 + y**2, (x, y)) for x, y in points]
        heapq.heapify(dists)
        results = [heapq.heappop(dists)[1] for _ in range(k)]
        return results
        