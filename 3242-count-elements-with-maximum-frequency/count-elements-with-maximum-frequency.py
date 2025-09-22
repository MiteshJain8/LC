class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        cnt = max(ctr.values())
        return sum(cnt if ctr[k] == cnt else 0 for k in ctr.keys())