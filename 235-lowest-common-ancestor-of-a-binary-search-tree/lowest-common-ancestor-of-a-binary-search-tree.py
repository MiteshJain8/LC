# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node):
            if node == p:
                return p
            if node == q:
                return q

            if p.val > node.val and q.val > node.val:
                return traverse(node.right)

            if p.val < node.val and q.val < node.val:
                return traverse(node.left)

            return node

        return traverse(root)