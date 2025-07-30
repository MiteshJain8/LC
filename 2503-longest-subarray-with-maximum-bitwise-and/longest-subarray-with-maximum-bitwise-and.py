class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        val_max = nums[0]
        res = 1
        cur_maxlen = 1
        for i in range(1, len(nums)):
            if nums[i] > val_max:
                val_max = nums[i]
                cur_maxlen = 1
                res = 1
            elif nums[i] == val_max:
                cur_maxlen += 1
                res = max(res, cur_maxlen)
            else:
                cur_maxlen = 0
                
        return res