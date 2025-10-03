class Solution:
    def trap(self, list1: List[int]) -> int:
        n = len(list1)
        res = 0
        left, right = 0, n - 1
        left_max, right_max = list1[0], list1[n-1]
        while left < right:
            if list1[left] < list1[right]:
                left += 1
                res += max(0, left_max - list1[left])
                left_max = max(left_max, list1[left])
            else:
                right -= 1
                res += max(0, right_max - list1[right])
                right_max = max(right_max, list1[right])

        return res