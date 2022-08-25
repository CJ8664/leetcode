# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                # If leaf node return depth
                if not curr.left and not curr.right:
                    return depth
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            # Increment depth after each level is traversed
            depth += 1
        return depth
                
        
        