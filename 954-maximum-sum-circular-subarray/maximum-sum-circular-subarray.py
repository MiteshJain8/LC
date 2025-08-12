class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        tot = 0
        curMax = curMin = 0
        resMax = resMin = nums[0]
        for num in nums:
            curMax = max(num, curMax + num)
            resMax = max(resMax, curMax)

            curMin = min(num, curMin + num)
            resMin = min(resMin, curMin)

            tot += num

        return resMax if tot == resMin else max(resMax, tot - resMin)