class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = 1
        while i < n:
            j = i
            while j + 1 < n and nums[j] < nums[j+1]: j+=1
            ans = max(ans, (j-i+1) // 2)
            k = j+1
            while k + 1 < n and nums[k] < nums[k+1]: k+=1
            ans = max(ans, min(j-i+1, k-j))
            i = j+1
        return ans