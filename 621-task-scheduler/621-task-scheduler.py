class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        h = [-x for x in counter.values()]
        heapq.heapify(h)
        q = deque()
        t = 0
        while h or q:
            t += 1
            if h:
                c = 1 + heapq.heappop(h)
                if c != 0:
                    q.append((c, t + n))
            if q and q[0][1] == t:
                heapq.heappush(h, q.popleft()[0])
        return t
            
        