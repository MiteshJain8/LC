class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cur = 0, 0
        prefixMap = defaultdict(int)
        prefixMap[0] += 1
        for e in nums:
            cur += e
            diff = cur - k
            res += prefixMap[diff]
            prefixMap[cur] += 1
        return res

