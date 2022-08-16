```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            # Append the task index to be used in forming the result
            task.append(idx)
        # So that we pick the the tasks by enqueued time
        tasks.sort()
     
        # We can start ts = 0 by we can fast forward to first known
        # enqued time
        i, ts = 0, tasks[0][0]
        pending_tasks, result = [], []
        
        # While there are pending tasks in the queue or we have not
        # enqueued all the tasks
        while pending_tasks or i < len(tasks):
            # Enqueue all the tasks which have enqueue time <= current ts
            while i < len(tasks) and tasks[i][0] <= ts:
                # Push the processing time, task index
                heapq.heappush(pending_tasks, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if pending_tasks:
                prc_time, task_idx = heapq.heappop(pending_tasks)
                result.append(task_idx)
                # Jump to next time stamp as we only process one task at a
                # time 
                ts += prc_time
            else:
                # If we dont have any tasks pending, jump to next ts when 
                # we have the task
                ts = tasks[i][0] 
        return result
                
                
            
            
        
            
            
            
        
```
