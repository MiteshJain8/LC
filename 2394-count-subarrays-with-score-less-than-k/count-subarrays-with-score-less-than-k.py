class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        j = 0
        while j < n and prefix[j] * (j+1) < k:
            j += 1
        res = j
        for i in range(1,n):
            while j < n and (prefix[j] - prefix[i-1]) * (j-i+1) < k:
                j += 1
            res += (j-i)
        return res
