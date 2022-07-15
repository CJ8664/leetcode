class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [((x**2 + y**2)**0.5, [x, y]) for x,y in points]
        heapq.heapify(dist)
        result = []
        for _ in range(k):
            _, point = heapq.heappop(dist)
            result.append(point)
        return result
        