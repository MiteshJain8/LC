class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(time):
            k = 0
            for rank in ranks:
                k += floor(sqrt(time/rank))
                if k >= cars:
                    return True
            return False 

        n = len(ranks)
        ranks.sort(reverse = True)
        left, right = ranks[-1] * ((cars//n) ** 2), ranks[0] * ((ceil(cars/n)) ** 2)
        res = 0
        while left <= right:
            mid = left + (right-left)//2
            if is_possible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res