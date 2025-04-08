class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        check = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in check:
                return ceil((i+1)/3)
            check.add(nums[i])
        return 0