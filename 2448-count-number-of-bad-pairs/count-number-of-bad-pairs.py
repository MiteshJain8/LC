class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hmap, n = defaultdict(int), len(nums)
        res = (n)*(n-1)//2
        for i in range(n):
            hmap[nums[i] - i] += 1
        for cnt in hmap.values():
            res -= (cnt)*(cnt-1)//2
        return res