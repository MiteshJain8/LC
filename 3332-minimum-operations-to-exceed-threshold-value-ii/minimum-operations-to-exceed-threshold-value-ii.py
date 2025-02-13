class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, x*2+y)
            res += 1
        return res