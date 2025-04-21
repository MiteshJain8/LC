class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev = maxi = mini = lower
        for diff in differences:
            prev += diff
            maxi = max(maxi, prev)
            mini = min(mini, prev)
        return max(0, upper-lower + mini-maxi + 1)