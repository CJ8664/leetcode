#!/usr/local/bin/python

# Problem URL : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def findHeight(self, node):
        if node is None:
            return 0
        else:
            left_height = self.findHeight(node.left)
            right_height = self.findHeight(node.right)
            
            if (left_height > right_height):
                return left_height + 1
            else:
                return right_height + 1
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return self.findHeight(root)
            