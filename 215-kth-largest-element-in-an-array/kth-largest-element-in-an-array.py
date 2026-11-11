class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -heappop(nums)