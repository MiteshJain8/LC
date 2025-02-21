# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hset = set()
        root.val = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                x = cur.val
                self.hset.add(x)
                if cur.left:
                    cur.left.val = 2*x+1
                    q.append(cur.left)
                if cur.right:
                    cur.right.val = 2*x+2
                    q.append(cur.right)

    def find(self, target: int) -> bool:
        return target in self.hset


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)