class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0
        for i in range(k+1):
            temp = [num for num in costs]
            for u,v,c in flights:
                if temp[v] > costs[u] + c:
                    temp[v] = costs[u] + c
            costs = temp
        return -1 if costs[dst] == float("inf") else costs[dst]