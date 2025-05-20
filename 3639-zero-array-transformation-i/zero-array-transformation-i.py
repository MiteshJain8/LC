class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pre_process = [0] * (n+1)
        cur_reduction = 0
        for l,r in queries:
            pre_process[l] += 1
            pre_process[r+1] -= 1
        for i in range(n):
            cur_reduction += pre_process[i]
            if cur_reduction < nums[i]:
                return False
        return True