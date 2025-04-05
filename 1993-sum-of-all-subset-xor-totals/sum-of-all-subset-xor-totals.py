class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, total):
            if i == len(nums):
                return total

            return backtrack(i+1, total) + backtrack(i+1, nums[i] ^ total)
        
        return backtrack(0, 0)