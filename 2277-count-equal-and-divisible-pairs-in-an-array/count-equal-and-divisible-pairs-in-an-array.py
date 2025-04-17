class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        idx_map = defaultdict(list)            

        for i in range(len(nums)):
            for j in idx_map[nums[i]]:
                if i*j % k == 0:
                    res += 1
            idx_map[nums[i]].append(i)
        return res