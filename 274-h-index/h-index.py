class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        i = n - 1
        while i >= 0 and citations[i] >= n - i:
            i -= 1

        return n - i - 1