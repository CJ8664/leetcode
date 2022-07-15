# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        
        q = collections.deque()
        q.append(root)
        result = []
        
        while q:
            level_value = None
            for _ in range(len(q)):
                node = q.popleft()
                level_value = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_value)
        return result
        
        