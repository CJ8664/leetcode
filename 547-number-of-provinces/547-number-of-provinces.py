class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_province = len(isConnected)
        # Array that stores the parent of a given node, initially
        # every node's parent is set itself
        ancestor = [i for i in range(num_province)]
        # Rank for each node
        rank = [1 for _ in range(num_province)]
        
        def find_ancestor(node):
            # While we dont reach to top most ancestor
            while node != ancestor[node]:
                # Path compression, for a give node, its grandparent is
                # is also a parent (ancestor) hence reduce the hop from 
                # child -> parent -> grandparent
                ancestor[node] = ancestor[ancestor[node]]
                # For the parent find its parent in the next iteration
                node = ancestor[node]
            # Should be the top most ancestor
            return node
                
        def union(node1, node2):
            node1_ancestor, node2_ancestor = find_ancestor(node1), find_ancestor(node2)
            # Both nodes have common ancestor, no need to union them
            if node1_ancestor == node2_ancestor:
                return 0
            
            # If node1 ancestor is elder (rank), ask node2 to merge into it
            # also, with the merge node1 ancestor is more elder now
            if rank[node1_ancestor] > rank[node2_ancestor]:
                ancestor[node2_ancestor] = node1_ancestor
                rank[node1_ancestor] += rank[node2_ancestor]
            else:
                ancestor[node1_ancestor] = node2_ancestor
                rank[node2_ancestor] += rank[node1_ancestor]
            return 1
                
        for node1 in range(len(isConnected)):
            for node2 in range(len(isConnected[0])):
                if isConnected[node1][node2] == 1:
                    num_province -= union(node1, node2)
        return num_province
        