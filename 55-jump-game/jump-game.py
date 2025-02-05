class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        valid_idx = N - 1
        
        for i in range(N - 2, -1, -1):
            if i + nums[i] >= valid_idx:
                valid_idx = i
        
        return valid_idx == 0