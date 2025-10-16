class Solution:
    def findSmallestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * k
        
        for v in nums:
            cnt[v % k] += 1

        for v in range(n + 1):
            if cnt[v % k] == 0:
                return v
            cnt[v % k] -= 1

        return n + 1