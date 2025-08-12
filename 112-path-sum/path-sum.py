# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node, curSum):
            if not node:
                return False
            if not node.left and not node.right:
                return curSum + node.val == targetSum

            return traverse(node.left, curSum + node.val) or traverse(node.right, curSum + node.val)

        return traverse(root, 0)