class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips=0
        for i in range(len(nums)-2):
            if not nums[i]:
                flips+=1
                nums[i], nums[i+1], nums[i+2]=1, not nums[i+1], not nums[i+2]
        if nums[-2:].count(0)==0:
            return flips
        return -1