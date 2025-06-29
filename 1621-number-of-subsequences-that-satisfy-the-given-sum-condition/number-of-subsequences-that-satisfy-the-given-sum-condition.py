class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 1e9 + 7
        nums.sort()
        n = len(nums)
        res = 0
        j = n-1
        power = [1] * n
        for i in range(1,n):
            power[i] = (power[i-1] * 2) % M
        for i in range(n):
            if nums[i] + nums[j] <= target:
                res += power[j-i]
                res %= M
            else:
                while i < j and nums[i] + nums[j] > target:
                    j -= 1
                if nums[i] + nums[j] <= target:
                    res += power[j-i]
                    res %= M
                else:
                    break
        return int(res)