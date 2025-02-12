class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        prefix = defaultdict(list)
        n, res = len(nums), -1
        for i in range(n):
            num = nums[i]
            dig = 0
            while num:
                dig += num % 10
                num //= 10
            heappush(prefix[dig], -nums[i])
        for pq in prefix.values():
            if len(pq) > 1:
                n1 = -heappop(pq)
                n2 = -heappop(pq)
                res = max(res, n1+n2)
        return res