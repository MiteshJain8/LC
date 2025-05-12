class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        j, l, n, res = 0, 0, len(nums), 0
        freq1, freq2 = defaultdict(int), defaultdict(int)
        for i in range(n):
            while j < n and len(freq1) < k:
                freq1[nums[j]] += 1
                j += 1
            while l < n and len(freq2) <= k:
                freq2[nums[l]] += 1
                l += 1
            if len(freq2) == k+1:
                res += (l-j)
            elif len(freq1) == k:
                res += (n-j+1)
            
            freq1[nums[i]] -= 1
            if (freq1[nums[i]] == 0): del freq1[nums[i]]
            freq2[nums[i]] -= 1
            if (freq2[nums[i]] == 0): del freq2[nums[i]]

        return res