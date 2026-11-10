class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if target == nums[0] else -1
        idx, res = 0, -1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                idx = i+1
                nums = nums[i+1:] + nums[:i+1]
                break
        l, r = 0, n-1
        while l <= r:
            m = (r-l)//2 + l
            if nums[m] == target:
                res = (idx + m) % n
                break
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return res
