class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        j = 0
        res = sorted(nums)
        idx = bisect.bisect_right(res, pivot)
        for i in range(len(nums)):
            if nums[i] < pivot:
                res[j] = nums[i]
                j += 1
            elif nums[i] > pivot:
                res[idx] = nums[i]
                idx += 1
        return res