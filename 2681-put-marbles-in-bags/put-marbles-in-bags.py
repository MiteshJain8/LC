class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
        costs = [0] * (n-1)
        for i in range(n-1):
            costs[i] = weights[i] + weights[i+1]
        costs.sort()
        return sum(costs[-k+1:]) - sum(costs[:k-1])