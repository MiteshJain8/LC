# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([(root, 0)])
        hmap = defaultdict(list)
        max_col, min_col = 0, 0
        while dq:
            local_map = defaultdict(list)
            for _ in range(len(dq)):
                node, cur_col = dq.popleft()
                local_map[cur_col].append(node.val)
                max_col = max(max_col, cur_col)
                min_col = min(min_col, cur_col)
                if node.left:
                    dq.append((node.left, cur_col - 1))
                if node.right:
                    dq.append((node.right, cur_col + 1))

            for k in local_map.keys():
                hmap[k] += sorted(local_map[k])

        return [hmap[c] for c in range(min_col, max_col + 1)]