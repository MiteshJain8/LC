# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        def backtrack(node, curSum):
            if not node.left and not node.right:
                return curSum == targetSum

            res = False
            if node.left:
                res = backtrack(node.left, node.left.val+curSum)
            if node.right:
                res = res or backtrack(node.right, node.right.val+curSum)
            return res

        return backtrack(root, root.val)