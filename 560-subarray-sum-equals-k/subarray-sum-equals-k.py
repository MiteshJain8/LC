class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        res = cur = 0
        for i in nums:
            cur += i
            diff = cur - k
            res += prefix[diff]
            prefix[cur] += 1
        return res