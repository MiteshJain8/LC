class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(val):
            i = n-1
            cur = 0
            while i >= 0 and cur < k:
                if candies[i] >= val:
                    cur += candies[i]//val
                    i -= 1
                else:
                    return False
            return cur >= k

        n = len(candies)
        Sum = sum(candies)
        if Sum < k:
            return 0
        candies.sort()
        left, right, res = 1, Sum//k, 0
        while left <= right:
            mid = left + (right-left)//2
            if possible(mid):
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res