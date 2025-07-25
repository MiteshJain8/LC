class Solution:
    def maxSum(self, nums: List[int]) -> int:
        cur_max = nums[0]
        n = len(nums)
        cnt = 0
        hset = set()
        for i in range(n):
            cur_max = max(cur_max, nums[i])
            if nums[i] in hset:
                nums[i] = 0
            if nums[i] < 0:
                nums[i] = 0
                cnt += 1
            hset.add(nums[i])

        return sum(nums) if cnt < n else cur_max