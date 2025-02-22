# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth, i = 0, 0
        stack = []
        n = len(traversal)
        while i < n:
            if traversal[i] == '-':
                depth += 1
                i += 1
            else:
                j = i
                while j < n and traversal[j].isdigit():
                    j += 1
                node = TreeNode(int(traversal[i:j]))
                while stack and depth < len(stack):
                    stack.pop()
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                i = j
                depth = 0
        return stack[0]
                