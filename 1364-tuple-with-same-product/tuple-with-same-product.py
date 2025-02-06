class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        n, res = len(nums), 0
        for i in range(n-1):
            for j in range(i+1, n):
                hmap[nums[i]*nums[j]] += 1
        for cnt in hmap.values():
            res += comb(cnt,2) * 8
        return res