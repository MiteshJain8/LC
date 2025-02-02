class Solution:
    def check(self, nums: List[int]) -> bool:
        flag, idx = True, 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if flag:
                    flag = False
                    idx = i
                else:
                    return False
        if idx:
            return nums[0] >= nums[-1]
        return True