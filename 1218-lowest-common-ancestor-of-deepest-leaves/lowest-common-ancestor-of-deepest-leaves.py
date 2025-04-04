# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def check(node, deep):
            if node == None:
                return deep, None
            
            (leftDeep, left) = check(node.left, deep + 1)
            (rightDeep, right) = check(node.right, deep + 1)
            if left == None and right == None:
                return deep, node
            if (not left) or (not right):
                return (leftDeep, left) if left else (rightDeep, right)
            if leftDeep == rightDeep:
                return leftDeep, node
            return (leftDeep, left) if leftDeep > rightDeep else (rightDeep, right)


        return check(root, 0)[1]