# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.counter = k
        def inOrder(root):
            if not root:
                return 
            
            inOrder(root.left)
            self.counter -= 1
            if self.counter == 0:
                self.result = root.val
            inOrder(root.right)
        inOrder(root)
        return self.result