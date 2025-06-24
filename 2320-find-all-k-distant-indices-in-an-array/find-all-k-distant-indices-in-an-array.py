class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        cur = 0
        n = len(nums)
        for i,val in enumerate(nums):
            if val == key:
                cur = max(cur, i - k)
                for idx in range(cur, min(n, i + k + 1)):
                    res.append(idx)
                cur = min(n, i + k + 1)
                if cur >= n:
                    break

        return res