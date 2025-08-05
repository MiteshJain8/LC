class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        occupied = [False] * n
        for f in fruits:
            for i in range(n):
                if baskets[i] >= f and not occupied[i]:
                    occupied[i] = True
                    break

        return occupied.count(False)