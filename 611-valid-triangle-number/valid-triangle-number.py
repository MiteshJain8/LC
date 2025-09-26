class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(n-1, 1, -1):
            j, k = i-1, 0
            while k < j:
                if nums[i] < nums[j] + nums[k]:
                    res += (j - k)
                    j -= 1
                else:
                    k += 1
                    
        return res