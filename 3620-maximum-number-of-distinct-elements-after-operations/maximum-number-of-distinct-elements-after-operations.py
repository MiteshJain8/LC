class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        temp = 0
        minL = 0
        maxR = 0
        cur = float('-inf')
        res = 0
        for i in range(len(nums)):
            minL = nums[i] - k
            maxR = nums[i] + k
            t = max(cur + 1 , minL)
            if(t <= maxR):
                res += 1
                cur = t
            else:
                continue
        return res