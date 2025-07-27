class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = nums[0]
        res = 0
        n = len(nums)
        for i in range(1, n-1):
            if prev < nums[i] and nums[i+1] < nums[i]:
                res += 1
                prev = nums[i+1]
            elif prev >= nums[i]:
                prev = nums[i]
            
        prev = nums[0]
        for i in range(1, n-1):
            if prev > nums[i] and nums[i+1] > nums[i]:
                res += 1
                prev = nums[i+1]
            elif prev <= nums[i]:
                prev = nums[i]
            
        return res