class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n, j = len(nums), 0
        res = sorted(nums)
        idx = res.index(pivot)
        while idx < n-1 and res[idx+1] == pivot:
            idx += 1
        idx += 1
        for i in range(n):
            if nums[i] < pivot:
                res[j] = nums[i]
                j += 1
            elif nums[i] > pivot:
                res[idx] = nums[i]
                idx += 1
        return res