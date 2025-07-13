class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapify(players)
        heapify(trainers)
        res = 0
        while players and trainers:
            if players[0] <= trainers[0]:
                res += 1
                heappop(players)
            heappop(trainers)

        return res