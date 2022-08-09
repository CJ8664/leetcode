# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, result, ltr = deque(), [], 1
        q.append(root)
        while q:
            level = deque()
            for _ in range(len(q)):
                curr = q.popleft()
                # Based on direction of current iteration append to right of 
                # list or append to left of list
                level.append(curr.val) if ltr == 1 else level.appendleft(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            result.append(level)
            # Toggle the direction
            ltr *= -1
        return result
                
                
        