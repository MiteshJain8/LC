class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev_crest = prev_trough = nums[0]
        res = 0
        for i in range(1, len(nums)-1):
            if prev_trough < nums[i] and nums[i+1] < nums[i]:
                res += 1
                prev_trough = nums[i+1]
            elif prev_trough >= nums[i]:
                prev_trough = nums[i]

            if prev_crest > nums[i] and nums[i+1] > nums[i]:
                res += 1
                prev_crest = nums[i+1]
            elif prev_crest <= nums[i]:
                prev_crest = nums[i]
            
        return res