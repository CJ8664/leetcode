class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ############################################
        #### Prims algo | Minimum spanning tree ####
        ############################################
        N = len(points)
        # Adjaceny list
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            (x1, y1) = points[i]
            for j in range(i + 1, N):
                (x2, y2) = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
                
        # For each point
        # 1. Add the distance for all the neighbor 
        # 2. Find the neighbor with the minimum distance from it.
        # 3. Add it to visited and also add its neighbors to the "frontier"
        # 4. Frontier is the set of all the candidate edges the we
        #    might want to connect
        
        # Initially the point zero has an edge to itself with distance 0
        mst = [(0, 0)]

        # Nodes that we have already added to the MST
        visited = set()
        result = 0
        while len(visited) < len(points):
            dist, point = heapq.heappop(mst)
            # Already added the point to MST
            if point in visited:
                continue
                
            visited.add(point)
            result += dist
                
            # Add all it neighbors to the frontier
            for neigh_dist, neigh in adj[point]:
                if neigh not in visited:
                    heapq.heappush(mst, (neigh_dist, neigh))
        return result
            
        