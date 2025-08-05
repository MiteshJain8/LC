class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for f in fruits:
            for i in range(n):
                if baskets[i] >= f:
                    baskets[i] = 0
                    break

        return n - baskets.count(0)