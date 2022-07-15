# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = preorder.pop(0)
        idx = inorder.index(root_val)
        left = self.buildTree(preorder, inorder[0:idx])
        right = self.buildTree(preorder, inorder[idx + 1:])
        return TreeNode(root_val, left, right)
        