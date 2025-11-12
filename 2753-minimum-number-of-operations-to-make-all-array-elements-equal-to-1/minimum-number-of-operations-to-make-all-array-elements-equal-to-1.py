class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = nums.count(1)
        if n1 > 0:
            return n - n1
        g = nums[0]
        for x in nums:
            g = gcd(g, x)
        if g != 1:
            return -1
        min_len = n
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        return min_len + n - 2