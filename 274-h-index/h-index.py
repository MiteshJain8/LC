class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        i = 0
        res = 0
        while i < n:
            if citations[i] >= i+1:
                res = max(i+1, res)
            i += 1
        return res