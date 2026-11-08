class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        prev, cur, nxt = 0, nums[n-2], nums[n-1]
        for i in range(n-3, -1, -1):
            prev = max(cur, nums[i] + nxt)
            nxt = max(nxt, cur)
            cur = prev
        return cur