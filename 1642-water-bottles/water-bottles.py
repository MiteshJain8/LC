class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            exchanges = numBottles // numExchange
            res += exchanges
            numBottles = exchanges + numBottles % numExchange

        return res