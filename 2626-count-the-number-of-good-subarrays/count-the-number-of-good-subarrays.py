class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res, n, i, pairs = 0, len(nums), 0, 0
        freq = defaultdict(int)
        for j in range(n):
            pairs += freq[nums[j]]
            freq[nums[j]] += 1
            while pairs >= k:
                res += (n-j)
                freq[nums[i]] -= 1
                pairs -= freq[nums[i]]
                i += 1
        return res