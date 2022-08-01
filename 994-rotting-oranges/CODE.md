```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_r, n_c = len(grid), len(grid[0])
        q = deque()
        rem = 0
        visited = set()
        time = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Get first batch of rotten oranges
        for r in range(n_r):
            for c in range(n_c):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    rem += 1
                    
        def infect_neighbor(r, c):
            new_infect = []
            for d_r, d_c in dirs:
                t_r, t_c = r + d_r, c + d_c
                if not (0 <= t_r < n_r) or not (0 <= t_c < n_c):
                    continue
                if grid[t_r][t_c] == 1:
                    new_infect.append((t_r, t_c))
                    visited.add((t_r, t_c))
                    grid[t_r][t_c] = 2
            return new_infect
                          
        prev_rem = rem     
        # While there are pending rotten oranges
        # or remaining fresh count i greater than zero
        while q and rem > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))

                # infect neighbor
                new_infect = infect_neighbor(r, c)
                rem -= len(new_infect)
                q.extend(new_infect)
            if rem == prev_rem:
                break
            prev_rem = rem   
        return time if rem == 0 else -1
            
        
        
        
```
