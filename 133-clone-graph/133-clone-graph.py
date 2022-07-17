"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy_node = Node(node.val)
            oldToNew[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(clone(neighbor))
            return copy_node
        
        return clone(node) if node else None
        
        