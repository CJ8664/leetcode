# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec: 
    # Cannot use preorder + inorder serialization because 
    # there can be duplicate nodes in a tree
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pre = []
        def preorder(node):
            if not node:
                pre.append("#")
            else:
                pre.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ",".join(pre)
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0 
        preorder = data.split(",")
        def helper():
            if self.idx >= len(preorder) or preorder[self.idx] == "#":
                self.idx += 1
                return None
            node = TreeNode(int(preorder[self.idx]))
            self.idx += 1
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))