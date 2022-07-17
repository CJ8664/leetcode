class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_r, n_c = len(heights), len(heights[0])
        pac, atl = set(), set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def explore(r, c, explored, prev_height):
            if not (0 <= r < n_r) or not (0 <= c < n_c) or (r, c) in explored:
                return
            if prev_height > heights[r][c]:
                return
            
            # Mark current as explored
            explored.add((r, c))
            for d_r, d_c in dirs:
                explore(r + d_r, c + d_c, explored, heights[r][c])
        
        # For each row check elements
        # - left column and travel inwards from pacific
        # - right column and travel inwards from atlantic
        for r in range(n_r):
            explore(r, 0, pac, heights[r][0])
            explore(r, n_c - 1, atl, heights[r][n_c - 1])
            
        # For each columns check elements
        # - top row and travel inwards from pacific
        # - right column and travel inwards from atlantic
        for c in range(n_c):
            explore(0, c, pac, heights[0][c])
            explore(n_r - 1, c, atl, heights[n_r - 1][c])
            
        # Return the set of elements that can be reached 
        # from both pacific and atlantic
        return [(r, c) for (r, c) in (pac & atl)]
            
        
        