# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque([root])
        res = []
        while dq:
            tot, cnt = 0, len(dq)
            for _ in range(cnt):
                node = dq.popleft()
                tot += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(tot/cnt)

        return res