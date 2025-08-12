# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0

            leftMax = max(0, traverse(node.left))
            rightMax = max(0, traverse(node.right))
            nonlocal maxSum
            maxSum = max(maxSum, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
            
        maxSum = float("-inf")
        traverse(root)
        return maxSum