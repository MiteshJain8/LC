# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        dq = deque([root])
        res = []
        while dq:
            k = len(dq)
            avg = 0
            for i in range(k):
                node = dq.popleft()
                avg += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(avg/k)
        return res