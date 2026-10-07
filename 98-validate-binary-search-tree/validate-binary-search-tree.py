# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def backtrack(node, less, greater):
            res = less < node.val < greater
            if node.left:
                res = res and backtrack(node.left, less, node.val)
            if node.right:
                res = res and backtrack(node.right, node.val, greater)
            return res


        return backtrack(root, float("-inf"), float("inf"))
