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
            if node.val in memory: return memory[node.val]
            
            # Create a clone and save in memory so that if the 
            # current node is someone's neighbor then they can
            # get the clone from memory
            node_clone = Node(val=node.val)
            memory[node.val] = node_clone
            
            for neig in node.neighbors:
                node_clone.neighbors.append(clone(neig))
            return node_clone
        
        return clone(node) if node else None
        
        
        