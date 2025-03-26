from statistics import median
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = grid[0][0] % x
        one_d_nums = []
        for arr in grid:
            for ele in arr:
                if ele % x != mod:
                    return -1
            one_d_nums += arr
        one_d_nums.sort()
        med = one_d_nums[m*n // 2]
        res = 0
        for num in one_d_nums:
            res += abs(med - num) // x
        return res