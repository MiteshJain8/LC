class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_possible(val):
            cur = i = 0
            while i < len(nums):
                if nums[i] <= val:
                    cur += 1
                    if cur == k:
                        return True
                    i += 1
                i += 1
            return False

        sizes = sorted(list(set(nums)))
        left, right, res = 0, len(sizes)-1, 0
        while left <= right:
            mid = left + (right-left)//2
            if is_possible(sizes[mid]):
                res = sizes[mid]
                right = mid - 1
            else:
                left = mid + 1
        return res