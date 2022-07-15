# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if root is None:
                res.append("#")
            else:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ",".join(res)

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.idx = 0
        def helper():
            if self.idx >= len(data) or data[self.idx] == "#":
                self.idx += 1
                return None
            
            root = TreeNode(data[self.idx])
            self.idx += 1
            root.left = helper()
            root.right = helper()
            return root
        
        return helper()
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))