"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        memory = {}
        def clone(node):
            if not node:
                return None
            
            if node.val in memory:
                return memory[node.val]
            
            node_clone = Node(val=node.val)
            memory[node.val] = node_clone
            
            for neig in node.neighbors:
                node_clone.neighbors.append(clone(neig))
            return node_clone
        
        return clone(node)
        
        
        