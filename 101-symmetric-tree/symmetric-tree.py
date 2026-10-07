# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def backtrack(l, r):
            if l and r:
                return l.val == r.val and backtrack(l.left, r.right) and backtrack(l.right, r.left)
            elif l or r:
                return False
            return True

        return backtrack(root.left, root.right)
