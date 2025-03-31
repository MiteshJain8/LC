class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
        for i in range(n-1):
            weights[i] = weights[i] + weights[i+1]
        weights.pop()
        weights.sort()
        return sum(weights[-k+1:]) - sum(weights[:k-1])