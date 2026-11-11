class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        if not n:
            return True
        cur = n - 1
        flag = True
        while cur >= 0:
            flag = False
            if cur + nums[cur] >= n:
                n = cur
                cur = n - 1
                flag = True
            else:
                cur -= 1
        return flag
