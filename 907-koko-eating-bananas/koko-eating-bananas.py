class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_poossible(k):
            rem = h
            for i in range(len(piles)):
                rem -= ceil(piles[i]/k)
                if rem < 0:
                    return False
            return rem >= 0 

        left, right, res = 1, max(piles), 0
        while left <= right:
            mid = left + (right-left)//2
            if is_poossible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res