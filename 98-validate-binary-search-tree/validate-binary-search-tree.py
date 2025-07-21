# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = TreeNode(float("-inf"))

        def inorder(node):
            nonlocal prev
            if not node:
                return True

            res = inorder(node.left)
            if prev.val >= node.val:
                return False

            prev = node
            return inorder(node.right) and res

        res = inorder(root)
        return res