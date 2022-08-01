```python
class PendingTask:
    __slots__ = ["remaining_units", "next_time"]
    def __init__(self, remaining_units, next_time):
        self.remaining_units = remaining_units
        self.next_time = next_time
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        ready_tasks = [-x for x in counter.values()]
        heapq.heapify(ready_tasks)
        pending_tasks = deque()
        curr_time = 0
        while ready_tasks or pending_tasks:
            curr_time += 1
            if ready_tasks:
                remaining_units = 1 + heapq.heappop(ready_tasks)
                if remaining_units != 0:
                    pending_tasks.append(PendingTask(remaining_units, curr_time + n))
            if pending_tasks and pending_tasks[0].next_time == curr_time:
                heapq.heappush(ready_tasks, pending_tasks.popleft().remaining_units)
        return curr_time
            
        
```
