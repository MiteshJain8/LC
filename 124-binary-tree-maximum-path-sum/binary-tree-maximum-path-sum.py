# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def maxSumTillNode(node):
            if not node:
                return 0
            nonlocal res
            leftN = maxSumTillNode(node.left)
            rightN = maxSumTillNode(node.right)
            if leftN > 0 and rightN > 0:
                res = max(res, leftN + node.val + rightN)
            elif leftN > 0:
                res = max(res, leftN, node.val + leftN)
            elif rightN > 0:
                res = max(res, rightN, node.val + rightN)
            else:
                res = max(res, node.val)
            return node.val + max(rightN, leftN, 0)

        res = float("-inf")
        maxSumTillNode(root)
        return res