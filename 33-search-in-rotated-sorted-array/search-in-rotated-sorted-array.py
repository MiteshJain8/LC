class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        start = 0
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] <= nums[n-1]:
                r = mid - 1
                start = mid
            elif nums[mid] > nums[n-1]:
                l = mid + 1

        end = start + n - 1
        while start <= end:
            mid = (end - start) // 2 + start
            idx = mid % n
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1