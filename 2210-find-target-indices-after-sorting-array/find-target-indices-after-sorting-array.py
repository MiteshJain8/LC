class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        eq, lt = 0, 0
        for e in nums:
            if e == target:
                eq += 1
            elif e < target:
                lt += 1
        return [i for i in range(lt, lt+eq)]